import logging
from pathlib import Path
from tqdm.auto import tqdm
import numpy as np
import time

from sparse_transform.qsft.utils.general import qary_ints, qary_vec_to_dec, gwht, load_data, save_data
from sparse_transform.qsft.signals.input_signal import Signal
from sparse_transform.qsft.utils.query import get_Ms_and_Ds

logger = logging.getLogger(__name__)

class SubsampledSignal(Signal):
    """
    A shell Class for input signal/functions that are too large and cannot be stored in their entirety. In addition to
    the signal itself, this must also contain information about the M and D matrices that are used for subsampling.

    Attributes
    ----------
    query_args : dict
        Parameters that determine the structure of the Ms and Ds needed for subsampling.
        - b : int
            The max dimension of subsampling.
        - all_bs : list, optional
            List of all the b values that should be subsampled.
        - subsampling_method : str
            Method for generating M matrices.
        - delays_method_channel : str
            Method for channel delays.
        - delays_method_source : str
            Method for source delays.
        - num_repeat : int
            Number of repetitions.
        - num_subsample : int
            Number of subsamples.
    L : np.array
        An array that enumerates all q^b q-ary vectors of length b.
    foldername : str
        Path to the folder for saving/loading data.
    """
    def _set_params(self, **kwargs):
        self.func = kwargs.get("func")
        self.n = kwargs.get("n")
        self.q = kwargs.get("q")
        self.N = self.q ** self.n
        self.noise_sd = kwargs.get("noise_sd")
        self.signal_w = kwargs.get("signal_w")
        self.query_args = kwargs.get("query_args")
        self.b = self.query_args.get("b")
        self.all_bs = self.query_args.get("all_bs", [self.b])   # all b values to sample/transform at
        self.num_subsample = self.query_args.get("num_subsample")
        if "num_repeat" not in self.query_args:
            self.query_args["num_repeat"] = 1
        self.num_repeat = self.query_args.get("num_repeat")
        self.subsampling_method = self.query_args.get("subsampling_method")
        self.delays_method_source = self.query_args.get("delays_method_source")
        self.delays_method_channel = self.query_args.get("delays_method_channel")
        self.L = None  # List of all length b qary vectors
        self.foldername = kwargs.get("folder")
        self.all_samples = []
        self.all_queries = []

    def _init_signal(self):
        if self.subsampling_method == "uniform":
            self._subsample_uniform()
        elif self.subsampling_method == "qsft":
            self._set_Ms_and_Ds_qsft()
            self._subsample_qsft()
            self._compute_transforms()
        else:
            raise NotImplementedError

    def _set_Ms_and_Ds_qsft(self):
        """
        Sets the values of Ms and Ds, either by loading from a folder if it exists, or by generating them from query_args.
        """
        if self.foldername:
            Path(f"{self.foldername}").mkdir(exist_ok=True)
            Ms_and_Ds_path = Path(f"{self.foldername}/Ms_and_Ds.pickle")
            if Ms_and_Ds_path.is_file():
                self.Ms, self.Ds = load_data(Ms_and_Ds_path)
            else:
                self.Ms, self.Ds = get_Ms_and_Ds(self.n, self.q, **self.query_args)
                save_data((self.Ms, self.Ds), f"{self.foldername}/Ms_and_Ds.pickle")
        else:
            self.Ms, self.Ds = get_Ms_and_Ds(self.n, self.q, **self.query_args)

    def _subsample_qsft(self):
        """
        Subsamples and computes the sparse Fourier transform for each subsampling group if the samples are not already
        present in the folder.
        """
        self.Us = [[{} for j in range(len(self.Ds[i]))] for i in range(len(self.Ms))]
        self.transformTimes = [[{} for j in range(len(self.Ds[i]))] for i in range(len(self.Ms))]

        if self.foldername:
            Path(f"{self.foldername}/samples").mkdir(exist_ok=True)

        self._compute_or_load_samples()

    def _compute_or_load_samples(self):
        """
        Computes or loads the samples for each subsampling group.
        """
        pbar_disable = logger.getEffectiveLevel() > logging.INFO
        pbar = tqdm(total=0, position=0, disable=pbar_disable, desc="[sparse-transform] Collecting samples")
        for i in range(len(self.Ms)):
            for j in range(len(self.Ds[i])):
                sample_file = Path(f"{self.foldername}/samples/M{i}_D{j}.pickle")
                query_indices = self._get_qsft_query_indices(self.Ms[i], self.Ds[i][j], dec=False)
                self.all_queries.append(query_indices)
                if self.foldername and sample_file.is_file():
                    samples = load_data(sample_file)
                    pbar.total = len(self.Ms) * len(self.Ds[0]) * len(samples)
                    pbar.update(len(samples))
                else:
                    block_length = len(query_indices[0])
                    samples = np.zeros((len(query_indices), block_length), dtype=complex)
                    pbar.total = len(self.Ms) * len(self.Ds[0]) * len(query_indices)
                    all_query_indices = np.concatenate(query_indices)
                    all_subs_samples = self.subsample(all_query_indices)
                    for k in range(len(query_indices)):
                        samples[k] = all_subs_samples[k * block_length: (k+1) * block_length]
                    pbar.update(len(query_indices))
                    pbar.refresh()
                    if self.foldername:
                        save_data(samples, sample_file)
                self.all_samples.append(samples)

    def _compute_transforms(self):
        """
        Compute the transforms for each subsampling group.
        """
        for i in range(len(self.Ms)):
            for j in range(len(self.Ds[i])):
                for b in self.all_bs:
                    start_time = time.time()
                    self.Us[i][j][b] = self._compute_subtransform(self.all_samples[i * len(self.Ds[i]) + j], b)
                    self.transformTimes[i][j][b] = time.time() - start_time

    def _subsample_uniform(self):
        """
        Uniformly subsamples the signal. Useful when solving via LASSO.
        """
        if self.foldername:
            Path(f"{self.foldername}").mkdir(exist_ok=True)

        sample_file = Path(f"{self.foldername}/signal_t.pickle")
        if self.foldername and sample_file.is_file():
            signal_t = load_data(sample_file)
        else:
            query_indices = self._get_random_query_indices(self.query_args["n_samples"])
            samples = self.subsample(query_indices)
            signal_t = dict(zip(query_indices, samples))
            if self.foldername:
                save_data(signal_t, sample_file)
        self.signal_t = signal_t

    def get_all_qary_vectors(self):
        """
        Retrieves all q-ary vectors of length b.

        Returns
        -------
        np.array
            Array of all q^b q-ary vectors.
        """
        if self.L is None:
            self.L = np.array(qary_ints(self.b, self.q))  # List of all length b qary vectors
        return self.L

    def subsample(self, query_indices):
        """
        Subsamples the signal based on the provided query indices.

        Parameters
        ----------
        query_indices : list
            Indices to query.

        Returns
        -------
        np.array
            Subsampled signal values.
        """
        if self.func is None:
            raise NotImplementedError
        else:
            return self.func(query_indices)

    def _get_qsft_query_indices(self, M, D_sub, dec=True):
        """
        Gets the indices to be queried for a given M and D.

        Parameters
        ----------
        M : np.array
            Matrix M.
        D_sub : np.array
            Subset of matrix D.
        dec : bool, optional
            Whether to return indices in decimal format. Defaults to True.

        Returns
        -------
        list
            Indices to be queried.
        """
        b = M.shape[1]
        L = self.get_all_qary_vectors()
        ML = (M @ L) % self.q
        base_inds = [(ML + np.outer(d, np.ones(self.q ** b, dtype=int))) % self.q for d in D_sub]
        base_inds = np.array(base_inds)
        if dec:
            base_inds_dec = []
            for i in range(len(base_inds)):
                base_inds_dec.append(qary_vec_to_dec(base_inds[i], self.q))
            return base_inds_dec
        else:
            base_inds_bin = []
            for i in range(len(base_inds)):
                base_inds_bin.append(base_inds[i].T)
            return base_inds_bin

    def _get_random_query_indices(self, n_samples):
        """
        Returns random indices to be sampled.

        Parameters
        ----------
        n_samples : int
            Number of samples to query.

        Returns
        -------
        list
            Indices to be queried in decimal representation.
        """
        queries = np.random.choice(self.q, size=(n_samples, self.n))
        return [tuple(row) for row in queries]


    def get_MDU(self, ret_num_subsample, ret_num_repeat, b, trans_times=False):
        """
        Retrieves the effective Ms, Ds, and Us (subsampled transforms).

        Parameters
        ----------
        ret_num_subsample : int
            Number of subsamples to return.
        ret_num_repeat : int
            Number of repetitions to return.
        b : int
            Dimension of subsampling.
        trans_times : bool, optional
            Whether to return transformation times. Defaults to False.

        Returns
        -------
        tuple
            Ms_ret, Ds_ret, Us_ret, and optionally Ts_ret if trans_times is True.
        """
        Ms_ret = []
        Ds_ret = []
        Us_ret = []
        Ts_ret = []
        if ret_num_subsample <= self.num_subsample and ret_num_repeat <= self.num_repeat and b <= self.b:
            subsample_idx = np.random.choice(self.num_subsample, ret_num_subsample, replace=False)
            delay_idx = np.random.choice(self.num_repeat, ret_num_repeat, replace=False)
            for i in subsample_idx:
                Ms_ret.append(self.Ms[i][:, :b])
                Ds_ret.append([])
                Us_ret.append([])
                Ts_ret.append([])
                for j in delay_idx:
                    Ds_ret[-1].append(self.Ds[i][j])
                    Us_ret[-1].append(self.Us[i][j][b])
                    Ts_ret[-1].append(self.transformTimes[i][j][b])
            if trans_times:
                return Ms_ret, Ds_ret, Us_ret, Ts_ret
            else:
                return Ms_ret, Ds_ret, Us_ret
        else:
            raise ValueError("There are not enough Ms or Ds.")

    def _compute_subtransform(self, samples, b):
        """
        Computes the subtransform for the given samples and dimension b.

        Parameters
        ----------
        samples : np.array
            Subsampled signal values.
        b : int
            Dimension of the subtransform.

        Returns
        -------
        list
            Computed subtransform.
        """
        transform = [gwht(row[::(self.q ** (self.b - b))], self.q, b) for row in samples]
        return transform

    def get_source_parity(self):
        """
        Retrieves the source parity.

        Returns
        -------
        int
            Source parity value.
        """
        return self.Ds[0][0].shape[0]

    @staticmethod
    def get_number_of_samples(n, b, t, q, query_args):
        """
        Compute the number of vector-wise calls to self.func.

        Parameters
        ----------
        n : int
            Input parameter n.
        b : int
            Input parameter b.
        t : int
            Input parameter t.
        q : int
            Input parameter q.
        query_args : dict
            Additional query arguments.

        Returns
        -------
        int
            The total number of calls to self.func.
        """
        num_subsample = query_args.get("num_subsample", 1)
        num_rows_per_D = SubsampledSignal._get_delay_overhead(n, t, query_args)
        samples_per_row = q ** b
        total_samples = num_subsample * num_rows_per_D * samples_per_row
        return total_samples

    @staticmethod
    def get_b_for_sample_budget(budget, n, t, q, query_args):
        """
        Find the maximum value of b that fits within the sample budget.

        Parameters
        ----------
        budget : int
            Maximum allowed number of samples.
        n : int
            Input parameter n.
        t : int
            Error parameter t.
        q : int
            Base of the transform.
        query_args : dict
            Additional query arguments.

        Returns
        -------
        int
            The maximum b that keeps the total samples within the budget.
        """
        num_subsample = query_args.get("num_subsample", 1)
        num_rows_per_D = SubsampledSignal._get_delay_overhead(n, t, query_args)
        largest_b = np.floor(np.log(budget / (num_rows_per_D * num_subsample)) / np.log(q))
        return int(largest_b)

    @staticmethod
    def _get_delay_overhead(n, t, query_args): # TODO depends on q in general
        """
        Returns the overhead of the delays in terms of the number of samples
        """
        delays_method_source = query_args.get("delays_method_source", "identity")
        if delays_method_source == "identity":
            num_rows_per_D = n + 1
        elif delays_method_source == "joint-coded":
            from sparse_transform.qsft.codes.BCH import BCH
            nc, kc = BCH.parameter_search(n, t)
            num_rows_per_D = nc - kc + 1  # BCH parity length + 1 (for zero row)
        elif delays_method_source == "random":
            # For random delays, the number is specified or defaulted
            num_rows_per_D = query_args.get("num_delays", n)
        else:
            # For other delay methods, assume default behavior
            num_rows_per_D = n + 1

        if query_args.get("delays_method_channel") == "nso":
            num_repeat = query_args.get("num_repeat", 1)
        else :
            num_repeat = 1
        return num_rows_per_D * num_repeat
