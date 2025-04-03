import logging
import time
import numpy as np
from sparse_transform.qsft.utils.general import bin_to_dec, binary_ints
from sparse_transform.qsft.codes.BCH import BCH
from functools import partial
from typing import List, Any, Callable, Union

logger = logging.getLogger(__name__)


def get_Ms_simple(n: int, b: int, **kwargs: Any) -> List[np.ndarray]:
    """
    Sets Ms[0] = [I 0 ...], Ms[1] = [0 I ...], Ms[2] = [0 0 I 0 ...] and so forth.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    Ms = []
    for i in range(kwargs["num_to_get"] - 1, -1, -1):
        M = np.zeros((n, b), dtype=int)
        M[(b * i) : (b * (i + 1)), :] = np.eye(b)
        Ms.append(M)
    return Ms

def get_Ms_complex(n: int, b: int, q: int, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate M uniformly at random.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    q : int
        Base of the transform.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    Ms = []
    for i in range(kwargs["num_to_get"]):
        M = np.random.randint(q, size=(n, b))
        Ms.append(M)
    return Ms

def get_Ms_parity(n: int, b: int, q: int, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate M uniformly at random with parity.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    q : int
        Base of the transform.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    Ms = []
    for i in range(kwargs["num_to_get"]):
        M = np.hstack((np.ones((n, 1), dtype=int), np.random.randint(q, size=(n, b-1))))
        Ms.append(M)
    return Ms

def get_Ms_antithetic(n: int, b: int, q: int, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate antithetic sampling matrix M.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    q : int
        Base of the transform.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    Ms = []
    for i in range(kwargs["num_to_get"]):
        M1 = np.random.randint(q, size=(n, b-1))
        M2 = (1 - M1[:, 0]).astype(int)
        M = np.hstack((M2[:, np.newaxis], M1))
        Ms.append(M)
    return Ms

def get_Ms_complex_low_degree(n: int, b: int, q: int, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate low degree M matrices.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    q : int
        Base of the transform.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    C = kwargs["num_to_get"]
    M = np.zeros((n, b * C), dtype=int)
    for i in range(b * C):
        for j in range(2**i):
            M[j::2**(i+1), i] = 1
    Ms = []
    for i in range(C):
        Ms.append(M[:, i*b:(i+1)*b])
    return Ms

def get_Ms(n: int, b: int, q: int, method: str = "simple", **kwargs: Any) -> List[np.ndarray]:
    """
    Gets subsampling matrices for different sparsity levels.

    Parameters
    ----------
    n : int
        Number of rows.
    b : int
        Number of columns.
    q : int
        Base of the transform.
    method : str
        Method to use for generating matrices.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        List of subsampling matrices.
    """
    if "num_to_get" not in kwargs:
        kwargs["num_to_get"] = max(n // b, 3)

    if method == "simple" and kwargs["num_to_get"] > n // b:
        raise ValueError("When query_method is 'simple', the number of M matrices to return cannot be larger than n // b")

    return {
        "simple": get_Ms_simple,
        "complex": get_Ms_complex,
        "complex_ld": get_Ms_complex_low_degree,
        "parity": get_Ms_parity,
        "antithetic": get_Ms_antithetic,
    }.get(method)(n=n, b=b, q=q, **kwargs)

def get_D_identity(n: int, **kwargs: Any) -> np.ndarray:
    """
    Generate identity delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    np.ndarray
        Identity delay matrix.
    """
    int_delays = np.zeros(n, )
    int_delays = np.vstack((int_delays, np.eye(n)))
    return int_delays.astype(int)

def get_D_random(n: int, **kwargs: Any) -> np.ndarray:
    """
    Generate random delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    np.ndarray
        Random delay matrix.
    """
    q=kwargs.get("q", 2)
    num_delays = kwargs.get("num_delays")
    return np.random.choice(q, (num_delays, n))

def get_D_joint_coded(n: int, **kwargs: Any) -> np.ndarray:
    """
    Generate joint coded delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    np.ndarray
        Joint coded delay matrix.
    """
    t = kwargs.get("t")
    D = BCH(n, t).get_delay_matrix()
    return np.array(D, dtype=int)

def get_D_nso(n: int, D_source: np.ndarray, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate NSO-SPRIGHT delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    D_source : np.ndarray
        Source delay matrix.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        NSO-SPRIGHT delay matrix.
    """
    num_repeat = kwargs.get("num_repeat")
    q = kwargs.get("q", 2)
    random_offsets = get_D_random(n, q=q, num_delays=num_repeat)
    D = []
    for row in random_offsets:
        modulated_offsets = (row - D_source) % q
        D.append(modulated_offsets)
    return D

def get_D_channel_coded(n: int, D: np.ndarray, **kwargs: Any) -> None:
    """
    Generate channel coded delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    D : np.ndarray
        Delay matrix.
    **kwargs : Any
        Additional keyword arguments.

    Raises
    ------
    NotImplementedError
        This function is not implemented.
    """
    raise NotImplementedError("One day this might be implemented")

def get_D_channel_identity(n: int, D: np.ndarray, **kwargs: Any) -> List[np.ndarray]:
    """
    Generate channel identity delay matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    D : np.ndarray
        Delay matrix.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    List[np.ndarray]
        Channel identity delay matrix.
    """
    q = kwargs.get("q", 2)
    return [D % q]

def get_D(n: int, **kwargs: Any) -> np.ndarray:
    """
    Delay generator: gets a delays matrix.

    Parameters
    ----------
    n : int
        Number of rows.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    np.ndarray
        Delays matrix.
    """
    delays_method_source = kwargs.get("delays_method_source", "random")
    D = {
        "random": get_D_random,
        "identity": get_D_identity,
        "joint-coded": get_D_joint_coded,
    }.get(delays_method_source)(n, **kwargs)

    delays_method_channel = kwargs.get("delays_method_channel", "identity")
    D = {
            "nso": get_D_nso,
            "coded": get_D_channel_coded,
            "identity": get_D_channel_identity,
            "identity-siso": get_D_channel_identity,
    }.get(delays_method_channel)(n, D, **kwargs)
    return D

def subsample_indices(M: np.ndarray, d: np.ndarray) -> np.ndarray:
    """
    Query generator: creates indices for signal subsamples.

    Parameters
    ----------
    M : np.ndarray
        Subsampling matrix.
    d : np.ndarray
        Subsampling offset.

    Returns
    -------
    np.ndarray
        Subsample indices.
    """
    L = binary_ints(M.shape[1])
    inds_binary = np.mod(np.dot(M, L).T + d, 2).T
    return bin_to_dec(inds_binary)

def get_Ms_and_Ds(n, q, **kwargs):
    """
    Based on the parameters provided in kwargs, generates Ms and Ds.

    Parameters
    ----------
    n : int
        Number of rows.
    q : int
        Base of the transform.
    **kwargs : Any
        Additional keyword arguments.

    Returns
    -------
    Tuple[List[np.ndarray], List[np.ndarray]]
        Subsampling matrices (Ms) and delay matrices (Ds).
    """
    query_method = kwargs.get("query_method")
    b = kwargs.get("b")
    num_subsample = kwargs.get("num_subsample")

    start_time = time.time()
    Ms = get_Ms(n, b, q, method=query_method, num_to_get=num_subsample)
    logger.debug(f"M Generation:{time.time() - start_time}")
    Ds = []
    
    start_time = time.time()
    D = get_D(n, q=q, **kwargs)
    logger.debug(f"D Generation:{time.time() - start_time}")

    for M in Ms:
        Ds.append(D)
    return Ms, Ds

def get_bch_decoder(n: int, t: int, dectype: str = "hard", chase_depth: Union[int, None] = None) -> Callable:
    """
    Gets a suitable BCH decoder.

    Parameters
    ----------
    n : int
        Number of rows.
    t : int
        Number of errors to correct.
    dectype : str
        Type of decoding.
    chase_depth : Union[int, None]
        Depth of chase decoding.

    Returns
    -------
    Callable
        BCH decoder.
    """
    if dectype == "hard":
        dec = BCH(n, t).parity_decode
    elif dectype == "soft" or dectype == "soft-list":
        dec = partial(BCH(n, t).parity_decode_2chase_t2_max_likelihood,
                      list_dec=(dectype == "ml-soft-t2-list"),
                      chase_depth=chase_depth)
    elif dectype == "soft-basic" or dectype == "soft-basic-list":
        dec = partial(BCH(n, t).parity_decode_2chase,
                      list_dec=(dectype == "soft-list"),
                      chase_depth=chase_depth)
    elif dectype == "subseq-soft-t2" or dectype == "subseq-soft-t2-list":
        dec = partial(BCH(n, t).parity_decode_2chase_t2,
                      list_dec=(dectype == "subseq-soft-t2-list"),
                      chase_depth=chase_depth)
    elif dectype == "subseq-soft-t2-opt" or dectype == "subseq-soft-t2-opt-list":
        dec = partial(BCH(n, t).parity_decode_2chase_t2,
                      list_dec=(dectype == "subseq-soft-t2-opt-list"),
                      chase_depth=chase_depth)
    else:
        dec = None
        raise NotImplementedError("Decoding type not implemented")
    return dec
