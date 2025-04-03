import numpy as np
import itertools
import math
import zlib
import pickle
import json
import heapq
import time
from scipy.spatial import ConvexHull
import scipy.fft as fft
from typing import List, Tuple, Union, Any

def gwht(x: np.ndarray, q: int, n: int) -> np.ndarray:
    """
    Computes the GWHT of an input array with forward scaling.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    q : int
        Base of the transform.
    n : int
        Dimension of the transform.

    Returns
    -------
    np.ndarray
        Transformed array.
    """
    x_tensor = np.reshape(x, [q] * n)
    x_tf = fft.fftn(x_tensor) / (q ** n)
    x_tf = np.reshape(x_tf, [q ** n])
    return x_tf

def gwht_tensored(x: np.ndarray, q: int, n: int) -> np.ndarray:
    """
    Computes the GWHT of a tensored input array with forward scaling.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    q : int
        Base of the transform.
    n : int
        Dimension of the transform.

    Returns
    -------
    np.ndarray
        Transformed array.
    """
    x_tf = fft.fftn(x) / (q ** n)
    return x_tf

def igwht(x: np.ndarray, q: int, n: int) -> np.ndarray:
    """
    Computes the IGWHT of an input array with forward scaling.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    q : int
        Base of the transform.
    n : int
        Dimension of the transform.

    Returns
    -------
    np.ndarray
        Transformed array.
    """
    x_tensor = np.reshape(x, [q] * n)
    x_tf = fft.ifftn(x_tensor) * (q ** n)
    x_tf = np.reshape(x_tf, [q ** n])
    return x_tf

def igwht_tensored(x: np.ndarray, q: int, n: int) -> np.ndarray:
    """
    Computes the IGWHT of a tensored input array with forward scaling.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    q : int
        Base of the transform.
    n : int
        Dimension of the transform.

    Returns
    -------
    np.ndarray
        Transformed array.
    """
    x_tf = fft.ifftn(x) * (q ** n)
    return x_tf

def bin_to_dec(x: np.ndarray) -> int:
    """
    Converts a binary array to a decimal integer.

    Parameters
    ----------
    x : np.ndarray
        Binary array.

    Returns
    -------
    int
        Decimal integer.
    """
    n = len(x)
    c = 2**(np.arange(n)[::-1])
    return c.dot(x).astype(int)

def nth_roots_unity(n: int) -> np.ndarray:
    """
    Computes the nth roots of unity.

    Parameters
    ----------
    n : int
        The order of the roots.

    Returns
    -------
    np.ndarray
        Array of nth roots of unity.
    """
    return np.exp(-2j * np.pi / n * np.arange(n))


def near_nth_roots(ratios: np.ndarray, q: int, eps: float) -> bool:
    """
    Checks if the given ratios are near the nth roots of unity.

    Parameters
    ----------
    ratios : np.ndarray
        Array of ratios.
    q : int
        Base of the transform.
    eps : float
        Tolerance.

    Returns
    -------
    bool
        True if the ratios are near the nth roots of unity, False otherwise.
    """
    in_set = np.zeros(ratios.shape, dtype=bool)
    omega = nth_roots_unity(q)
    for i in range(q):
        in_set = in_set | (np.square(np.abs(ratios - omega[i])) < eps)
    is_singleton = in_set.all()
    return is_singleton

def qary_vec_to_dec(x: np.ndarray, q: int = 2) ->  Union[np.int64, np.int32, object]:
    """
    Converts a q-ary vector to a decimal integer.

    Parameters
    ----------
    x : np.ndarray
        q-ary vector.
    q : int
        Base of the vector.

    Returns
    -------
    int
        Decimal integer.
    """
    n = x.shape[0]
    return np.array([q ** (n - (i + 1)) for i in range(n)], dtype=object) @ np.array(x,  dtype=object)


def dec_to_qary_vec(x: int, q: int, n: int) -> np.ndarray:
    """
    Converts a decimal integer to a q-ary vector.

    Parameters
    ----------
    x : int
        Decimal integer.
    q : int
        Base of the vector.
    n : int
        Length of the vector.

    Returns
    -------
    np.ndarray
        q-ary vector.
    """
    qary_vec = []
    for i in range(n):
        qary_vec.append(np.array([a // (q ** (n - (i + 1))) for a in x], dtype=object))
        x = x - (q ** (n-(i + 1))) * qary_vec[i]
    return np.array(qary_vec, dtype=int)

def binary_ints(m: int) -> np.ndarray:
    """
    Returns a matrix where row 'i' is the binary representation of 'i', for 'i' from 0 to 2 ** m - 1.

    Parameters
    ----------
    m : int
        Number of bits.

    Returns
    -------
    np.ndarray
        Matrix of binary representations.
    """
    a = np.arange(2 ** m, dtype=int)[np.newaxis,:]
    b = np.arange(m, dtype=int)[::-1,np.newaxis]
    return np.array(a & 2**b > 0, dtype=int)

def angle_q(x: np.ndarray, q: int) -> np.ndarray:
    """
    Computes the q-ary angle of a complex array.

    Parameters
    ----------
    x : np.ndarray
        Complex array.
    q : int
        Base of the angle.

    Returns
    -------
    np.ndarray
        q-ary angle array.
    """
    return (((np.angle(x) % (2*np.pi) // (np.pi/q)) + 1) // 2) % q # Can be made much faster

def qary_ints(m: int, q: int, dtype: type = int) -> np.ndarray:
    """
    Returns a matrix of all q-ary vectors of length m.

    Parameters
    ----------
    m : int
        Length of the vectors.
    q : int
        Base of the vectors.
    dtype : type
        Data type of the vectors.

    Returns
    -------
    np.ndarray
        Matrix of q-ary vectors.
    """
    return np.array(list(itertools.product(np.arange(q), repeat=m)), dtype=dtype).T

def comb(n: int, k: int) -> int:
    """
    Computes the binomial coefficient "n choose k".

    Parameters
    ----------
    n : int
        Total number of items.
    k : int
        Number of items to choose.

    Returns
    -------
    int
        Binomial coefficient.
    """
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def qary_ints_low_order(m: int, q: int, order: int) -> np.ndarray:
    """
    Returns a matrix of all q-ary vectors of length m with a given order.

    Parameters
    ----------
    m : int
        Length of the vectors.
    q : int
        Base of the vectors.
    order : int
        Order of the vectors.

    Returns
    -------
    np.ndarray
        Matrix of q-ary vectors.
    """
    num_of_ks = np.sum([comb(m, o) * ((q-1) ** o) for o in range(order + 1)])
    K = np.zeros((num_of_ks, m))
    counter = 0
    for o in range(order + 1):
        positions = itertools.combinations(np.arange(m), o)
        for pos in positions:
            K[counter:counter+((q-1) ** o), pos] = np.array(list(itertools.product(1 + np.arange(q-1), repeat=o)))
            counter += ((q-1) ** o)
    return K.T

def random_signal_strength_model(sparsity: int, a: float, b: float) -> np.ndarray:
    """
    Generates a random signal strength model.

    Parameters
    ----------
    sparsity : int
        Sparsity of the signal.
    a : float
        Minimum magnitude.
    b : float
        Maximum magnitude.

    Returns
    -------
    np.ndarray
        Random signal strength model.
    """
    magnitude = np.random.uniform(a, b, sparsity)
    phase = np.random.uniform(0, 2*np.pi, sparsity)
    return magnitude * np.exp(1j*phase)


def random_skewed_signal_strength_model(sparsity: int, a: float, b: float, skewed: float) -> np.ndarray:
    """
    Generates a random skewed signal strength model.

    Parameters
    ----------
    sparsity : int
        Sparsity of the signal.
    a : float
        Minimum magnitude.
    b : float
        Maximum magnitude.
    skewed : float
        Skewness of the signal.

    Returns
    -------
    np.ndarray
        Random skewed signal strength model.
    """
    x_0 = a
    x_1 = b
    magnitude = np.power(np.linspace(x_0, x_1, sparsity),  (-1*skewed))
    signs = (2*(np.random.uniform(0, 1, sparsity) > 0.5).astype(int)) - 1
    return np.random.permutation(magnitude * signs)

def sort_qary_vecs(qary_vecs: np.ndarray) -> np.ndarray:
    """
    Sorts q-ary vectors.

    Parameters
    ----------
    qary_vecs : np.ndarray
        Input q-ary vectors.

    Returns
    -------
    np.ndarray
        Sorted q-ary vectors.
    """
    qary_vecs = np.array(qary_vecs)
    idx = np.lexsort(qary_vecs.T[::-1, :])
    return qary_vecs[idx]

def calc_hamming_weight(qary_vecs: np.ndarray) -> np.ndarray:
    """
    Calculates the Hamming weight of q-ary vectors.

    Parameters
    ----------
    qary_vecs : np.ndarray
        Input q-ary vectors.

    Returns
    -------
    np.ndarray
        Hamming weights.
    """
    qary_vecs = np.array(qary_vecs)
    return np.sum(qary_vecs != 0, axis = 1)

def save_data(data: Any, filename: str) -> None:
    """
    Saves data to a file.

    Parameters
    ----------
    data : Any
        Data to be saved.
    filename : str
        Name of the file.
    """
    with open(filename, 'wb') as f:
        f.write(zlib.compress(pickle.dumps(data, pickle.HIGHEST_PROTOCOL), 9))

def load_data(filename: str) -> Any:
    """
    Loads data from a compressed pickle file.

    Parameters
    ----------
    filename : str
        The name of the file to load data from.

    Returns
    -------
    Any
        The data loaded from the file.
    """
    start = time.time()
    with open(filename, 'rb') as f:
        data = pickle.loads(zlib.decompress(f.read()))
    return data

def k_smallest_partial_sums_with_indices(arr: List[float], k: int) -> List[Tuple[float, List[int]]]:
    """
    Finds the k smallest partial sums and their corresponding indices.

    Parameters
    ----------
    arr : list of float
        The input array of numbers.
    k : int
        The number of smallest partial sums to find.

    Returns
    -------
    list of tuple
        A list of tuples, each containing a partial sum and the corresponding indices.
    """
    h = []
    heapq.heappush(h, (0, [0]*len(arr)))
    for i in range(len(arr)):
        current_min = h[0][0]
        # add to the heap
        to_add = []
        for x in h:
            if len(h) < k or x[0] - arr[i] >= current_min:
                to_add.append((x[0] - arr[i], [x[1][j] if j != i else 1 for j in range(len(x[1]))]))
        if len(to_add) > 0:
            for el in to_add:
                heapq.heappush(h, el)
        # cull the heap
        if len(h) > k:
            h = heapq.nlargest(k, h)[::-1]
    return list(h)

def powerset(iterable, min_size=0, max_size=None):
    if max_size is None:
        max_size = len(iterable)
    s = sorted(list(iterable))
    max_size = len(s) if max_size is None else min(max_size, len(s))
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(max(min_size, 0),  max_size + 1))

def fourier_to_mobius(fourier_transform):
    moebius_dict = {}
    for loc, coef in fourier_transform.items():
        for subset in powerset(loc):
            scaling_factor = np.power(-2.0, len(subset))
            if subset in moebius_dict:
                moebius_dict[subset] += coef * scaling_factor
            else:
                moebius_dict[subset] = coef * scaling_factor
    return moebius_dict

if __name__ == '__main__':
    print(k_smallest_partial_sums_with_indices([0, 0.1, 0.5, 1.0, 2.0, 4.0], 3))
    print(k_smallest_partial_sums_with_indices([0, 0.1, 0.5, 1.0, 2.0, 4.0], 6))

