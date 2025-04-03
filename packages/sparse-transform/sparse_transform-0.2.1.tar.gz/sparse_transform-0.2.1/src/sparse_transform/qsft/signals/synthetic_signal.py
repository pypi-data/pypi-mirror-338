import logging 
import numpy as np
import time
from sparse_transform.qsft.utils.general import (igwht_tensored, random_signal_strength_model, qary_vec_to_dec,
                                                 sort_qary_vecs, random_skewed_signal_strength_model)
from .input_signal import Signal
from .input_signal_subsampled import SubsampledSignal

logger = logging.getLogger(__name__)

def generate_signal_w(n, q, sparsity, a_min, a_max, noise_sd=0, full=True, max_weight=None, skewed=False):
    """
    Generates a signal with sparse Fourier transform.

    Parameters
    ----------
    n : int
        The number of dimensions.
    q : int
        The base of the Fourier transform.
    sparsity : int
        The sparsity level of the signal.
    a_min : float
        Minimum amplitude of the signal.
    a_max : float
        Maximum amplitude of the signal.
    noise_sd : float, optional
        Standard deviation of the noise, by default 0.
    full : bool, optional
        If True, returns the full signal, by default True.
    max_weight : int, optional
        Maximum Hamming weight of the signal, by default None.
    skewed : bool, optional
        If True, generates a skewed signal, by default False.

    Returns
    -------
    Tuple
        A tuple containing:
        - np.ndarray: The generated signal in the Fourier domain.
        - np.ndarray: The locations of the non-zero coefficients in q-ary format.
        - np.ndarray: The strengths of the non-zero coefficients.
    """
    max_weight = n if max_weight is None else max_weight
    N = q ** n

    if max_weight == n:
        locq = sort_qary_vecs(np.random.randint(q, size=(n, sparsity)).T).T
    else:
        non_zero_idx_vals = np.random.randint(q - 1, size=(max_weight, sparsity)) + 1
        non_zero_idx_pos = np.random.choice(a=n, size=(sparsity, max_weight))
        locq = np.zeros((n, sparsity), dtype=int)
        for i in range(sparsity):
            locq[non_zero_idx_pos[i, :], i] = non_zero_idx_vals[:, i]
        locq = sort_qary_vecs(locq.T).T

    loc = qary_vec_to_dec(locq, q)
    if not skewed:
        strengths = random_signal_strength_model(sparsity, a_min, a_max)
    else:
        strengths = random_skewed_signal_strength_model(sparsity, a_min, a_max, skewed)
    if full:
        wht = np.zeros((N,), dtype=complex)
        for l, s in zip(loc, strengths):
            wht[l] = s
        signal_w = wht + np.random.normal(0, noise_sd, size=(N, 2)).view(complex).reshape(N)
        return np.reshape(signal_w, [q] * n), locq, strengths
    else:
        signal_w = dict(zip(list(map(tuple, locq.T)), strengths))
        return signal_w, locq, strengths


def get_random_signal(n, q, noise_sd, sparsity, a_min, a_max):
    """
    Computes a full random time-domain signal, which is sparse in the frequency domain.

    Parameters
    ----------
    n : int
        The number of dimensions.
    q : int
        The base of the Fourier transform.
    noise_sd : float
        Standard deviation of the noise.
    sparsity : int
        The sparsity level of the signal.
    a_min : float
        Minimum amplitude of the signal.
    a_max : float
        Maximum amplitude of the signal.

    Returns
    -------
    SyntheticSignal
        A synthetic signal object containing the generated signal.
    """
    signal_w, locq, strengths = generate_signal_w(n, q, sparsity, a_min, a_max, noise_sd, full=True)
    signal_t = igwht_tensored(signal_w, q, n)
    signal_params = {
        "n": n,
        "q": q,
        "noise_sd": noise_sd,
        "signal_t": signal_t,
        "signal_w": signal_w,
        "folder": "test_data"
    }
    return SyntheticSignal(locq, strengths, **signal_params)


class SyntheticSignal(Signal):
    """
    A synthetic signal object.

    This is essentially just a signal object, except the strengths and locations of the non-zero indices are known and
    included as attributes.

    Attributes
    ----------
    locq : np.ndarray
        Locations of the non-zero coefficients in q-ary format.
    strengths : np.ndarray
        Strengths of the non-zero coefficients.
    """

    def __init__(self, locq, strengths, **kwargs):
        """
        Initializes the SyntheticSignal object.

        Parameters
        ----------
        locq : np.ndarray
            Locations of the non-zero coefficients in q-ary format.
        strengths : np.ndarray
            Strengths of the non-zero coefficients.
        **kwargs
            Additional parameters for the Signal base class.
        """
        super().__init__(**kwargs)
        self.locq = locq
        self.strengths = strengths


def get_random_subsampled_signal(n, q, noise_sd, sparsity, a_min, a_max, query_args, max_weight=None, skewed=False):
    """
    Generates a random subsampled signal.

    Similar to `get_random_signal`, but instead of returning a `SyntheticSignal` object, it returns a
    `SyntheticSubsampledSignal` object. The advantage of this is that a subsampled signal does not compute the time-domain
    signal on creation but instead creates it on the fly. This should be used when `n` is large or when sampling is
    expensive.

    Parameters
    ----------
    n : int
        The number of dimensions.
    q : int
        The base of the Fourier transform.
    noise_sd : float
        Standard deviation of the noise.
    sparsity : int
        The sparsity level of the signal.
    a_min : float
        Minimum amplitude of the signal.
    a_max : float
        Maximum amplitude of the signal.
    query_args : dict
        Arguments for querying the signal.
    max_weight : int, optional
        Maximum Hamming weight of the signal, by default None.
    skewed : bool, optional
        If True, generates a skewed signal, by default False.

    Returns
    -------
    SyntheticSubsampledSignal
        A synthetic subsampled signal object.
    """
    start_time = time.time()
    signal_w, locq, strengths = generate_signal_w(n, q, sparsity, a_min, a_max, noise_sd, full=False,
                                                  max_weight=max_weight, skewed=skewed)
    signal_params = {
        "n": n,
        "q": q,
        "query_args": query_args,
    }
    logger.debug(f"Generation Time: {time.time() - start_time}", flush=True)
    return SyntheticSubsampledSignal(signal_w=signal_w, locq=locq, strengths=strengths,
                                     noise_sd=noise_sd, **signal_params)


class SyntheticSubsampledSignal(SubsampledSignal):
    """
    A synthetic subsampled signal object.

    This is a subsampled signal object, except it implements the unimplemented `subsample` function.

    Attributes
    ----------
    q : int
        The base of the Fourier transform.
    n : int
        The number of dimensions.
    locq : np.ndarray
        Locations of the non-zero coefficients in q-ary format.
    noise_sd : float
        Standard deviation of the noise.
    sampling_function : callable
        Function to compute signal values at queried indices.
    """

    def __init__(self, **kwargs):
        """
        Initializes the SyntheticSubsampledSignal object.

        Parameters
        ----------
        **kwargs
            Parameters for the SubsampledSignal base class.
        """
        self.q = kwargs["q"]
        self.n = kwargs["n"]
        self.locq = kwargs["locq"]
        self.noise_sd = kwargs["noise_sd"]
        freq_normalized = (2j * np.pi * kwargs["locq"].T / kwargs["q"]).T
        strengths = kwargs["strengths"]
        self.all_samples = []
        self.all_queries = []

        def sampling_function(query_batch):
            return np.exp(query_batch @ freq_normalized) @ strengths

        self.sampling_function = sampling_function

        super().__init__(**kwargs)

    def subsample(self, query_indices):
        """
        Computes the signal/function values at the queried indices on the fly.

        Parameters
        ----------
        query_indices : np.ndarray
            Indices to query.

        Returns
        -------
        np.ndarray
            Signal values at the queried indices.
        """
        samples = self.sampling_function(query_indices)
        return samples

    def get_MDU(self, ret_num_subsample, ret_num_repeat, b, trans_times=False):
        """
        Wraps the `get_MDU` method from SubsampledSignal to add synthetic noise.

        Parameters
        ----------
        ret_num_subsample : int
            Number of subsamples to return.
        ret_num_repeat : int
            Number of repetitions.
        b : int
            Parameter `b` used in the transformation.
        trans_times : bool, optional
            If True, returns transformation times, by default False.

        Returns
        -------
        Tuple
            A tuple containing the MDU matrices with added synthetic noise.
        """
        mdu = super().get_MDU(ret_num_subsample, ret_num_repeat, b, trans_times)
        for i in range(len(mdu[2])):
            for j in range(len(mdu[2][i])):
                size = np.array(mdu[2][i][j]).shape
                nu = self.noise_sd / np.sqrt(2 * self.q ** b)
                mdu[2][i][j] += np.random.normal(0, nu, size=size + (2,)).view(complex).reshape(size)
        return mdu
