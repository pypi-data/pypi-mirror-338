from typing import Dict, List, Tuple, Optional, Union, Any, Literal

import time
import random
import copy
import numpy as np
from functools import partial
import logging

from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, OrthogonalMatchingPursuit
from sparse_transform.qsft.utils.reconstruct import singleton_detection
from sparse_transform.qsft.utils.general import (qary_vec_to_dec, sort_qary_vecs, calc_hamming_weight,
                                                  dec_to_qary_vec, qary_ints_low_order)
from sparse_transform.qsft.signals.input_signal_subsampled import SubsampledSignal

logger = logging.getLogger(__name__)

def transform(
    signal: SubsampledSignal,
    reconstruct_method_source: Literal["identity", "coded"],
    reconstruct_method_channel: Literal["mle", "nso", "identity", "identity-siso"],
    b: int,
    num_subsample: int,
    num_repeat: int,
    source_decoder: Optional[Any] = None,
    report: bool = False,
    sort: bool = False,
    noise_sd: float = 0.0,
    peeling_method: Literal["multi-detect", "single-detect"] = "multi-detect",
    refined: bool = False,
    regress: Optional[Literal['linear', 'lasso', 'ridge']] = None,
    peel_average: bool = True,
    probabalistic_peel: bool = False,
    trap_exit: bool = True,
    res_energy_cutoff: float = 0.9,
) -> Dict:
    """
    Computes the q-ary Fourier transform of a signal object.

    Parameters
    ----------
    signal : SubsampledSignal
        The signal object to be transformed.
    reconstruct_method_source : {'identity', 'coded'}
        Method for source reconstruction.
    reconstruct_method_channel : {'mle', 'nso', 'identity', 'identity-siso'}
        Method for channel reconstruction.
    b : int
        Parameter `b` used in the transformation.
    num_subsample : int
        Number of subsamples.
    num_repeat : int
        Number of repetitions.
    source_decoder : Optional[Any], optional
        Optional decoder for the source, by default None.
    report : bool, optional
        If True, outputs detailed information about the time taken for each transform step, by default False.
    sort : bool, optional
        If True, returns the locations sorted in lexicographical order, by default False.
    noise_sd : float, optional
        Standard deviation of noise to be added, by default 0.0.
    peeling_method : {'multi-detect', 'single-detect'}, optional
        Peeling method to use, by default "multi-detect".
    refined : bool, optional
        If True, uses refined estimation, by default False.
    regress : {'linear', 'lasso', 'ridge'}, optional
        Regression method to use, by default None.
    peel_average : bool, optional
        If True, averages peeling results across bins, by default False.
    probabalistic_peel : bool, optional
        If True, uses probabilistic peeling, by default False.
    trap_exit : bool, optional
        If True, exits on trap condition, by default True.
    res_energy_cutoff : float, optional
        Cutoff for residual energy, by default 0.9.

    Returns
    -------
    Dict
        Dictionary containing the transform results.
    """
    q = signal.q
    n = signal.n

    omega = np.exp(2j * np.pi / q)
    result = []
    transform_dict = {}

    # import data
    if isinstance(signal, SubsampledSignal):
        Ms, Ds, Us, Ts = signal.get_MDU(num_subsample, num_repeat, b, trans_times=True)
    else:
        raise NotImplementedError("QSFT currently only supports signals that inherit from SubsampledSignal")
    for i in range(len(Ds)):
        Us[i] = np.vstack(Us[i])
        Ds[i] = np.vstack(Ds[i])
    if regress in ["freq_domain", "freq_domain_lasso"]:
        initial_Us = copy.deepcopy(Us)
    transform_time = np.sum(Ts)
    logger.debug(f"Transform Time:{transform_time}")
    Us = np.array(Us)
    if refined:
        samples = np.array(signal.all_samples).flatten()
        indicies = np.reshape(signal.all_queries, (len(samples), n))

        def refine_from_data(k_vec):
            nonlocal samples
            nonlocal indicies
            active = [i for i in range(len(k_vec)) if k_vec[i] == 1]
            signs = 1 - 2 * (np.sum(indicies[:, active], 1) % 2)
            inner_prod = sum(signs * samples)
            return inner_prod / len(samples)

    # Peeling Parameters
    peeling_max = q ** n
    peeled = set([])
    gamma = 0.5
    max_iter = 100
    peeled_at_iter = [0] * max_iter
    cutoff = 1e-9 + (1 + gamma) * (noise_sd ** 2) / (q ** b)  # noise threshold
    iter_step = 0
    cont_peeling = True
    num_peeling = 0
    multiton_count = 0
    zeroton_count = 0
    c = len(Ms)
    B = q ** b
    to_check = [[True] * B for _ in range(c)]
    logging.info(to_check)
    peeling_start = time.time()
    logging.info(f"cutoff = {cutoff}")
    logging.info(f"res_energy_cutoff = {res_energy_cutoff}")
    check_disable = False

    ####################################################################################################################
    # Peeling Loop
    ####################################################################################################################
    while cont_peeling and num_peeling < peeling_max and iter_step < max_iter:
        logger.debug(f"iter {iter_step}")
        singletons = {}  # dictionary from (i, j) values to the true index of the singleton, k (peelable).
        multitons = []  # list of (i, j) values indicating where multitons are (too hard to peel).
        ################################################################################################################
        # Step 1: Identify potential coefficients to peel by going through every bin
        ################################################################################################################
        for i, (U, M, D) in enumerate(zip(Us, Ms, Ds)):
            for j, col in enumerate(U.T):
                j_qary = dec_to_qary_vec([j], q, b).T[0]
                valid_k_partial = partial(valid_k,
                                          col=col,
                                          j_qary=j_qary,
                                          M=M,
                                          D=D,
                                          q=q,
                                          res_energy_cutoff=res_energy_cutoff,
                                          cutoff=cutoff,
                                          peeling_method=peeling_method,
                                          )
                if np.linalg.norm(col) ** 2 > cutoff * len(col) and (to_check[i][j] or check_disable):
                    k = singleton_detection(
                        col,
                        method_channel=reconstruct_method_channel,
                        method_source=reconstruct_method_source,
                        q=q,
                        source_parity=signal.get_source_parity(),
                        nso_subtype="nso1",
                        source_decoder=source_decoder,
                        valid_k=valid_k_partial,
                    )
                    # This exists only because we currently can't peel multiple k from the same bin in the same iter
                    if type(k) == list:
                        any_bin_matching = [np.all((M.T @ k_el) % q == j_qary) for k_el in k]
                        matching_count = 0
                        cw = -1
                        for k_i in range(len(k)):
                            if any_bin_matching[k_i]:
                                matching_count += 1
                                cw = k[k_i]
                        if type(cw) == int:
                            bin_matching = False
                            k = k[0]
                        else:
                            k = cw
                            bin_matching = True
                        if matching_count > 1:
                            logger.warning("Warning: list-decoding is working, but is not being exploited")
                        logger.log(5, f"Multi-detection output more than 1 Codeword!")
                    is_singleton, rho, residual = valid_k_partial(k)
                    logger.log(5, f"({i}, {j}), res: {np.linalg.norm(residual) ** 2}, thresh: {cutoff * len(col)}")
                    logger.log(5, f"frac. energy left: {(np.linalg.norm(residual) ** 2)/(np.linalg.norm(col) ** 2)}")
                    if (not is_singleton) or (probabalistic_peel and (random.random() < 0.2)):
                        multitons.append((i, j))
                        to_check[i][j] = is_singleton
                        logger.log(5, "We have a Multiton (Un-peelable)")
                    else:  # declare as singleton
                        if refined:
                            refined_rho = refine_from_data(k)
                            logger.log(5, f"Value refined from {rho}->{refined_rho}")
                            rho = refined_rho
                        singletons[(i, j)] = (k, rho)
                        logger.log(5, f"We have a Singleton at " + "[" + " ".join(map(str, k)) + "]")
                else:
                    if to_check[i][j]:
                        logger.log(5, f" ({i}, {j}) We have a Zeroton (nothing here)")
                    else:
                        logger.log(5, f" ({i}, {j}) skipping, nothing new.")
                    to_check[i][j] = False
        # all singletons and multitons are discovered
        logger.debug('singletons:')
        for ston in singletons.items():
            logger.debug(f"\t {ston[0]} {qary_vec_to_dec(ston[1][0], q)}")
        logger.debug("Multitons : {0}\n".format(multitons))
        multiton_count = len(multitons)
        zeroton_count = len(Us) * (q ** b) - len(singletons) - len(multitons)
        logger.debug(f"{iter_step, zeroton_count, multiton_count}")

        ################################################################################################################
        # Step 2: Peel those peelable terms
        ################################################################################################################
        # if there were no singletons, terminate
        if not check_disable:
            cont_peeling = any(any(to_check[i]) for i in range(len(to_check)))
        elif len(singletons) == 0:
            cont_peeling = False
        if trap_exit:
            if iter_step >= 15 and peeled_at_iter[iter_step-1] == peeled_at_iter[iter_step - 15]:
                cont_peeling = False
        # balls to peel
        balls_to_peel = set()
        ball_values = {}
        peeled_counter = {}
        for (i, j) in singletons:
            k, rho = singletons[(i, j)]
            ball = tuple(k)  # Must be a hashable type
            if peel_average:
                if ball in peeled_counter:
                    rho = (ball_values[ball] * peeled_counter[ball] + rho)/(peeled_counter[ball] + 1)
                    peeled_counter[ball] += 1
                else:
                    peeled_counter[ball] = 1
            balls_to_peel.add(ball)
            ball_values[ball] = rho
        logger.debug('these balls will be peeled')
        logger.debug(balls_to_peel)
        # peel
        for ball in balls_to_peel:
            num_peeling += 1
            k = np.array(ball)[..., np.newaxis]
            potential_peels = [(l, qary_vec_to_dec(M.T.dot(k) % q, q)[0]) for l, M in enumerate(Ms)]
            result.append((k.T[:][0], ball_values[ball], iter_step))
            k_dec = int(qary_vec_to_dec(k, q)[0])
            peeled.add(k_dec)
            logger.debug(f"Processing Singleton [{k_dec}]")
            logger.debug(k.T)
            for (l, j) in potential_peels:
                logger.debug("The singleton appears in M({0}), U({1})".format(l, j))

            for peel in potential_peels:
                signature_in_stage = omega ** (Ds[peel[0]] @ k)
                to_subtract = ball_values[ball] * signature_in_stage.reshape(-1, 1)
                logger.debug("Peeled ball {0} off bin {1}".format(qary_vec_to_dec(k, q), peel))
                Us[peel[0]][:, peel[1]] -= np.array(to_subtract)[:, 0]
                to_check[peel[0]][peel[1]] = True
            logger.debug("Iteration Complete: The peeled indicies are:")
            logger.debug(np.sort(list(peeled)))
        peeled_at_iter[iter_step] = len(peeled)
        iter_step += 1
    ####################################################################################################################
    # Step 3: Do some summing if we peeled the same index multiple times
    ####################################################################################################################
    loc = set()
    for k, value, iter_step in result:
        loc.add(tuple(k))
        transform_dict[tuple(k)] = transform_dict.get(tuple(k), 0) + value
    peeling_time = time.time() - peeling_start
    logger.debug(f"Peeling Time:{peeling_time}")
    ####################################################################################################################
    # Step 4: Format the output as required
    ####################################################################################################################
    if not report:
        return transform_dict
    else:
        n_samples = np.prod(np.shape(np.array(Us)))
        if len(loc) > 0:
            loc = list(loc)
            if sort:
                loc = sort_qary_vecs(loc)
            avg_hamming_weight = np.mean(calc_hamming_weight(loc))
            max_hamming_weight = np.max(calc_hamming_weight(loc))
        else:
            loc, avg_hamming_weight, max_hamming_weight = [], 0, 0
        result = {
            "transform": transform_dict,
            "runtime": transform_time + peeling_time,
            "n_samples": n_samples,
            "locations": loc,
            "avg_hamming_weight": avg_hamming_weight,
            "max_hamming_weight": max_hamming_weight,
            "fail_low_noise": len(loc) == 0 and zeroton_count <= 10,
            "fail_high_noise": len(loc) == 0 and multiton_count <= 10,
        }
        regress_start = time.time()
        if regress is not None:
            if regress == "freq_domain":
                new_transform_dict, _ = freq_domain_regression(result, n, b, initial_Us, Ms, Ds, Us)
            else:
                new_transform_dict, _ = fit_regression(regress, result, signal, n, b)
            result['transform'] = new_transform_dict
            logger.debug(f"Regression Time:{time.time() - regress_start}")
        return result


def valid_k(
    k: np.ndarray,
    col: np.ndarray,
    j_qary: np.ndarray,
    M: np.ndarray,
    D: np.ndarray,
    q: int,
    res_energy_cutoff: float,
    cutoff: float,
    peeling_method: str
) -> Tuple[bool, complex, np.ndarray]:
    """
    Validates if a given vector `k` is a singleton based on the provided parameters.

    Parameters
    ----------
    k : np.ndarray
        The vector to be validated.
    col : np.ndarray
        The column vector from the subsampled signal.
    j_qary : np.ndarray
        The q-ary representation of the index `j`.
    M : np.ndarray
        The matrix used in the QSFT algorithm.
    D : np.ndarray
        The matrix used in the QSFT algorithm.
    q : int
        The base of the q-ary Fourier transform.
    res_energy_cutoff : float
        The cutoff for the residual energy.
    cutoff : float
        The noise threshold.
    peeling_method : str
        Peeling method.

    Returns
    -------
    Tuple[bool, complex, np.ndarray]
        A tuple containing:
        - bool: Whether `k` is a valid singleton.
        - complex: The estimated coefficient `rho`.
        - np.ndarray: The residual vector.
    """
    omega = np.exp(2j * np.pi / q)
    signature = omega ** (D @ k)
    rho = np.dot(np.conjugate(signature), col) / D.shape[0]
    residual = col - rho * signature
    bin_matching = np.all((M.T @ k) % q == j_qary)
    if peeling_method == "multi-detect":
        # Check if the residual has less than x% of the remaining energy
        peel_condition = (np.linalg.norm(residual) ** 2) / (np.linalg.norm(col) ** 2) < res_energy_cutoff
    elif peeling_method == "single-detect":
        # Check if the residual is small
        peel_condition = np.linalg.norm(residual) ** 2 < cutoff * len(col)
    else:
        raise ValueError(f"Invalid peeling method: {peeling_method}")
    return (peel_condition and bin_matching), rho, residual


def fit_regression(
    type: str,
    results: Dict[str, Any],
    signal: SubsampledSignal,
    n: int,
    b: int
) -> Tuple[Dict[Tuple[int, ...], float], np.ndarray]:
    """
    Fits a regression model to the given signal data.

    Parameters
    ----------
    type : {'linear', 'lasso', 'ridge'}
        The type of regression model to use.
    results : Dict[str, Any]
        A dictionary containing the results of the transformation.
    signal : SubsampledSignal
        The signal object containing the data to be used for regression.
    n : int
        The length of the signal.
    b : int
        The number of bits used in the transformation.

    Returns
    -------
    Tuple[Dict[Tuple[int, ...], float], np.ndarray]
        A tuple containing:
        - dict: Regression coefficients for each support location.
        - np.ndarray: Support locations used in the regression.
    """
    assert type in ['linear', 'lasso', 'ridge']
    coordinates = []
    values = []
    for m in range(len(signal.all_samples)):
        for d in range(len(signal.all_samples[0])):
            for z in range(2 ** b):
                coordinates.append(signal.all_queries[m][d][z])
                values.append(np.real(signal.all_samples[m][d][z]))

    coordinates = np.array(coordinates)
    values = np.array(values)

    if len(results['locations']) == 0:
        support = np.zeros((1,n))
    else:
        support = results['locations']

    support = np.vstack([support, np.zeros(n), np.eye(n)])
    support = np.unique(support, axis=0)

    X = np.real(np.exp(coordinates @ (1j * np.pi * support.T)))
    alphas = [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]
    if type == 'linear':
        reg = LinearRegression(fit_intercept=False).fit(X, values)
    elif type == 'lasso':
        reg = LassoCV(fit_intercept=False, cv=5, alphas=alphas).fit(X, values).fit(X, values)
    elif type == 'ridge':
        reg = RidgeCV(fit_intercept=False, cv=5, alphas=alphas).fit(X, values).fit(X, values)

    regression_coefs = {}
    for coef in range(support.shape[0]):
        regression_coefs[tuple(support[coef, :].astype(int))] = reg.coef_[coef]

    return regression_coefs, support

def freq_domain_regression(
    results: Dict[str, Any],
    n: int,
    b: int,
    Us: List[np.ndarray],
    Ms: List[np.ndarray],
    Ds: List[np.ndarray],
    res_Us: List[np.ndarray],
    add_linear: bool = False,
) -> Tuple[Dict[Tuple[int, ...], float], np.ndarray]:
    """
    Perform frequency domain regression to refine the results of the QSFT algorithm.

    Parameters
    ----------
    results : Dict[str, Any]
        The initial results from the QSFT algorithm.
    n : int
        The length of the signal.
    b : int
        The number of bits used in the QSFT algorithm.
    Us : List[np.ndarray]
        A list of matrices representing the subsampled signal in the frequency domain.
    Ms : List[np.ndarray]
        A list of matrices used in the QSFT algorithm.
    Ds : List[np.ndarray]
        A list of matrices used in the QSFT algorithm.
    res_Us : List[np.ndarray]
        A list of residual matrices used in the regression process.
    add_linear : bool, optional
        If True, adds linear terms to support if many are not peeled, by default False.

    Returns
    -------
    Tuple[Dict[Tuple[int, ...], float], np.ndarray]
        A tuple containing:
        - dict: Refined coefficients for the support locations.
        - np.ndarray: Array of the support locations.
    """
    # Preprocess data
    if len(results['locations']) == 0:
        support = np.zeros((1,n))
        add_linear = True
    else:
        support = results['locations']
    support = np.vstack([support, np.zeros(n)])
    if add_linear:
        # add linear terms to support if many are not peeled
        support = np.vstack([support, np.eye(n)])
    support = np.unique(support, axis=0)

    # Pre-process the data
    k_to_idx = {}
    connected_variables = {}
    for idx, k in enumerate(support):
        for i, M in enumerate(Ms):
            j = qary_vec_to_dec(M.T.dot(k) % 2, 2)
            connected_variables[(i, j)] = connected_variables.get((i, j), []) + [k]
        k_to_idx[tuple(k)] = idx
    num_measurements = len(Us) * Us[0].shape[0] * Us[0].shape[1]
    num_variables = len(support)
    num_bin_samples = Us[0].shape[0]
    num_group_samples = Us[0].shape[0] * Us[0].shape[1]

    # Build the measurement matrix A and the vector b
    A = np.zeros(shape=(num_measurements, num_variables))
    b = np.zeros(shape=(num_measurements,))
    weights = np.ones(shape=(num_measurements,))
    for i, (U, M, D, res_U) in enumerate(zip(Us, Ms, Ds, res_Us)):
        for j, col in enumerate(U.T):
            res = np.real(res_U[:, j])
            b_part = np.real(col)
            start_idx = i * num_group_samples + j * num_bin_samples
            end_idx = start_idx + num_bin_samples
            b[start_idx:end_idx] = b_part
            weights[start_idx:end_idx] = np.var(res)
            vars = connected_variables.get((i, j), [])
            if not vars:
                continue
            vars_np = np.array(vars)
            var_idx = [k_to_idx[tuple(var)] for var in vars]
            A_part = (-1) ** (D @ vars_np.T)
            A[start_idx:end_idx, var_idx] = A_part

    reg = LinearRegression(fit_intercept=False).fit(A, b, sample_weight=1 / weights)

    regression_coefs = {}
    for coef in range(support.shape[0]):
        regression_coefs[tuple(support[coef, :].astype(int))] = reg.coef_[coef]
    return regression_coefs, support

def transform_via_omp(
    signal: SubsampledSignal,
    b: int,
    order: int
) -> Dict[str, Any]:
    """
    Transforms the given signal using Orthogonal Matching Pursuit (OMP).

    Parameters
    ----------
    signal : SubsampledSignal
        The signal object to be transformed.
    b : int
        The number of bits used in the transformation.
    order : int
        The order of the q-ary integers to be used.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing:
        - transform: Dictionary mapping support locations to coefficients.
        - runtime: Time taken for the transformation.
        - n_samples: Number of samples used.
        - locations: Set of support locations.
    """
    start_time = time.time()
    coordinates = []
    values = []
    for m in range(len(signal.all_samples)):
        for d in range(len(signal.all_samples[0])):
            for z in range(2 ** b):
                coordinates.append(signal.all_queries[m][d][z])
                values.append(np.real(signal.all_samples[m][d][z]))

    coordinates = np.array(coordinates)
    values = np.array(values)
    support = qary_ints_low_order(m=signal.n, q=signal.q, order=order).astype(int).T
    X = np.real(np.exp(coordinates @ (1j * np.pi * support.T)))
    omp = OrthogonalMatchingPursuit()
    omp.fit(X, values)
    coefficients = omp.coef_
    result = {}
    result['transform'] = {tuple(support[i]): coefficients[i] for i in range(len(coefficients)) if coefficients[i] != 0}
    result['runtime'] = time.time() - start_time
    result['n_samples'] = len(values)
    result['locations'] = result['transform'].keys()
    return result
