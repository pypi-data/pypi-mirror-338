import unittest
import numpy as np
import logging

import sparse_transform
from sparse_transform import qsft
from sparse_transform.qsft.utils.query import get_bch_decoder
from sparse_transform.qsft.signals.synthetic_signal import get_random_subsampled_signal

class TestQSFT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up logging
        logging.basicConfig(filename='tests/qsft_test.log', level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info('Started')

        sparse_transform.set_logging_level(logging.INFO)
        
        # Set random seed
        np.random.seed(5)
        
        # Initialize parameters
        cls.q = 2
        cls.n = 10
        cls.N = cls.q ** cls.n
        cls.b = 4
        cls.t = 4
        cls.max_weight = 2
        cls.noise_sd = 0
        cls.sparsity = 10
        cls.num_subsample = 3
        cls.num_repeat = 1
        cls.p = 0.6

        # Get decoder
        cls.decoder = get_bch_decoder(cls.n, cls.t, dectype="subseq-soft-t2-opt", chase_depth=3*cls.t)

        # Set up query and QSFT arguments
        cls.query_args = {
            "query_method": "complex",
            "num_subsample": cls.num_subsample,
            "delays_method_source": "joint-coded",
            "subsampling_method": "qsft",
            "delays_method_channel": "identity-siso",
            "num_repeat": cls.num_repeat,
            "b": cls.b,
            "t": cls.t
        }
        
        cls.qsft_args = {
            "num_subsample": cls.num_subsample,
            "num_repeat": cls.num_repeat,
            "reconstruct_method_source": "coded",
            "reconstruct_method_channel": "identity-siso",
            "b": cls.b,
            "source_decoder": cls.decoder
        }

        # Generate test signal
        cls.test_signal = get_random_subsampled_signal(
            n=cls.n,
            q=cls.q,
            noise_sd=cls.noise_sd,
            sparsity=cls.sparsity,
            a_min=1,
            a_max=10,
            query_args=cls.query_args,
            max_weight=cls.max_weight,
            skewed=cls.p,
        )


    def test_qsft_transform(self):
        """Test QSFT transformation"""
        result_qsft = qsft.transform(
            self.test_signal,
            report=True,
            sort=True,
            noise_sd=self.noise_sd,
            **self.qsft_args,
            regress=None,
            peel_average=True,
            probabalistic_peel=False,
            trap_exit=True,
        )
        self.assertIsNotNone(result_qsft)

    # def test_omp_transform(self):
    #     """Test OMP transformation"""
    #     result_omp = qsft.transform_via_omp(self.test_signal, b=self.b, order=2)
    #     self.assertIsNotNone(result_omp)

    # def test_amp_transform(self):
    #     """Test AMP transformation"""
    #     result_amp = qsft.transform_via_amp(self.test_signal, b=self.b, order=2)
    #     self.assertIsNotNone(result_amp)

if __name__ == '__main__':
    unittest.main()
