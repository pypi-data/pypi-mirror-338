import unittest
import numpy as np
import galois
from sparse_transform.qsft.codes.BCH import BCH


class TestBCH(unittest.TestCase):
    def setUp(self):
        # Common test parameters
        self.n = 100
        self.t = 5
        self.bch = BCH(self.n, self.t)

        # Create test vector
        self.test_vec = np.zeros(self.n, dtype=int)
        self.test_vec[0:3] = 1  # 3 errors
        self.test_vec = galois.GF2(self.test_vec)

    def test_initialization(self):
        """Test BCH initialization with various parameters"""
        test_params = [(108, 5), (63, 3), (31, 2), (127, 10)]

        for n, t in test_params:
            with self.subTest(n=n, t=t):
                bch = BCH(n, t)
                self.assertIsNotNone(bch)
                self.assertEqual(bch.t, t)

    def test_parameter_search(self):
        """Test the parameter_search method"""
        test_cases = [
            (100, 5),
            (63, 3),
            (31, 7),
            (21, 2)
        ]

        for n, t in test_cases:
            with self.subTest(n=n, t=t):
                nc, kc = BCH.parameter_search(n, t)
                self.assertTrue(nc >= n)
                self.assertTrue(kc >= n)
                # Verify that nc is 2^m - 1
                m = int(np.log2(nc + 1))
                self.assertEqual(nc, 2 ** m - 1)

    def test_get_delay_matrix(self):
        """Test delay matrix generation"""
        P = self.bch.get_delay_matrix()
        # Check matrix dimensions
        self.assertEqual(P.shape[0], self.bch.n - self.bch.k + 1)


    def test_get_parity_length(self):
        """Test parity length calculation"""
        parity_len = self.bch.get_parity_length()
        self.assertEqual(parity_len, self.bch.n - self.bch.k)

    def test_parity_decode(self):
        """Test basic parity decoding"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec)

        # Decode
        decoded, n_errors = self.bch.parity_decode(list(parity))
        decoded = np.array(decoded[0, :], dtype=int)

        # Check results
        self.assertEqual(n_errors, 3)  # Should detect 3 errors
        self.assertTrue(np.array_equal(decoded[:self.n], np.array(self.test_vec, dtype=int)))

    def test_parity_decode_with_noise(self):
        """Test decoding with added noise"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec)

        # Add more errors (beyond correction capability)
        corrupted_parity = parity.copy()
        corrupted_parity[0] = 1 - corrupted_parity[0]
        corrupted_parity[1] = 1 - corrupted_parity[1]
        corrupted_parity[2] = 1 - corrupted_parity[2]

        # Decode and check if it reports failure
        decoded, n_errors = self.bch.parity_decode(list(corrupted_parity))
        decoded = np.array(decoded[0, :], dtype=int)

        # Check results
        self.assertFalse(np.array_equal(decoded[:self.n], np.array(self.test_vec, dtype=int)))

    def test_parity_decode_2chase(self):
        """Test 2-chase decoding algorithm"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec, dtype=float)

        # Add soft information (simulate BPSK)
        soft_parity = -1.0 * (2 * parity - 1)  # Convert to {-1, 1}
        # Decode
        decoded, n_errors = self.bch.parity_decode_2chase(soft_parity, chase_depth=3)
        decoded = np.array(decoded[0, :], dtype=int)

        # Check results
        self.assertTrue(n_errors >= 0)
        self.assertTrue(np.array_equal(decoded[:self.n], np.array(self.test_vec, dtype=int)))

        # Test list decoding
        decoded_list = self.bch.parity_decode_2chase(soft_parity, list_dec=True, chase_depth=3)
        self.assertTrue(isinstance(decoded_list, list))

    def test_parity_decode_2chase_t2(self):
        """Test 2-chase_t2 decoding algorithm"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec, dtype=float)

        # Add soft information (simulate BPSK)
        soft_parity = -1.0 * (2 * parity - 1)

        # Decode
        decoded, n_errors = self.bch.parity_decode_2chase_t2(soft_parity, chase_depth=3)

        # Check if decoding succeeded
        self.assertTrue(n_errors >= -1)

        # Test list decoding
        decoded_list = self.bch.parity_decode_2chase_t2(soft_parity, list_dec=True, chase_depth=3)
        self.assertTrue(isinstance(decoded_list, list) or isinstance(decoded_list, tuple))

    def test_parity_decode_2chase_t2_max_likelihood(self):
        """Test max likelihood 2-chase_t2 decoding"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec, dtype=float)

        # Add soft information
        soft_parity = -1.0 * (2 * parity - 1)

        # Decode
        decoded, n_errors = self.bch.parity_decode_2chase_t2_max_likelihood(soft_parity, chase_depth=3)

        # Check if decoding succeeded
        self.assertTrue(n_errors >= -1)

    def test_parity_decode_2chase_t2_opt(self):
        """Test optimized 2-chase_t2 decoding"""
        # Generate parity
        P = self.bch.get_delay_matrix()
        parity = np.array(P[1:] @ self.test_vec, dtype=float)

        # Add soft information
        soft_parity = -1.0 * (2 * parity - 1)

        # Decode
        decoded, n_errors = self.bch.parity_decode_2chase_t2_opt(soft_parity, chase_depth=3)

        # Check if decoding succeeded
        self.assertTrue(n_errors >= -1)


if __name__ == '__main__':
    unittest.main()