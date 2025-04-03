import logging
import numpy as np
from pathlib import Path
from sparse_transform.qsft.utils.general import gwht_tensored, igwht_tensored, save_data, load_data

logger = logging.getLogger(__name__)

class Signal:
    """
    Encapsulates a time domain signal and its q-ary Fourier transform.

    Attributes
    ----------
    n : int
        Number of bits, representing the number of function inputs.
    q : int
        Alphabet size.
    noise_sd : float
        The standard deviation of the added noise.
    signal_t : np.ndarray
        Time domain representation of the signal.
    signal_w : np.ndarray
        Frequency domain representation of the signal.
    calc_w : bool
        If True and signal_w is not provided, it is computed based on signal_t.
    foldername : str
        Folder path for saving or loading the signal.
    is_synt : bool
        Indicates whether the signal is synthetic.
    """

    def __init__(self, **kwargs):
        """
        Initializes the Signal object.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments to set signal parameters.
        """
        self._set_params(**kwargs)
        self._init_signal()

    def _set_params(self, **kwargs):
        """
        Sets the parameters for the Signal object.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments to set signal parameters.
        """
        self.n = kwargs.get("n")
        self.q = kwargs.get("q")
        self.noise_sd = kwargs.get("noise_sd")
        self.N = self.q ** self.n
        self.signal_t = kwargs.get("signal_t")
        self.signal_w = kwargs.get("signal_w")
        self.calc_w = kwargs.get("calc_w", False)
        self.foldername = kwargs.get("folder")
        self.is_synt = False

    def _init_signal(self):
        """
        Initializes the signal by loading it from a file or generating a new one.
        """
        if self.signal_t is None:
            signal_path = Path(f"{self.foldername}/signal_t.pickle")
            if signal_path.is_file():
                self.signal_t = load_data(Path(f"{self.foldername}/signal_t.pickle"))
            else:
                self.sample()
                Path(f"{self.foldername}").mkdir(exist_ok=True)
                save_data(self.signal_t, Path(f"{self.foldername}/signal_t.pickle"))

        if self.calc_w and self.signal_w is None:
            self.signal_w = gwht_tensored(self.signal_t, self.q, self.n)
            if np.linalg.norm(self.signal_t - igwht_tensored(self.signal_w, self.q, self.n)) / self.N < 1e-5:
                logger.debug("verified transform")

    def sample(self):
        """
        Generates a new signal.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    def shape(self):
        """
        Returns the shape of the time domain signal.

        Returns
        -------
        tuple
            Shape of the time domain signal.
        """
        return tuple([self.q for i in range(self.n)])

    def get_time_domain(self, inds):
        """
        Queries the time domain signal at specific indices.

        Parameters
        ----------
        inds : tuple
            Tuple of 1D n-element arrays representing the indices to be queried.

        Returns
        -------
        np.ndarray
            Linear output of the queried indices.
        """
        inds = np.array(inds)
        if len(inds.shape) == 3:
            return [self.signal_t[tuple(inds)] for inds in inds]
        elif len(inds.shape) == 2:
            return self.signal_t[tuple(inds)]
