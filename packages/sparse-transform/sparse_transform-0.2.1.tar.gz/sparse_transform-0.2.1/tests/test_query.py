import unittest
import numpy as np
from sparse_transform.qsft.utils.query import (
    get_Ms_simple, get_Ms_complex, get_Ms_parity, get_Ms_antithetic,
    get_Ms_complex_low_degree, get_Ms, get_D_identity, get_D_random,
    get_D_joint_coded, get_D_nso, get_D_channel_identity,
    get_D, subsample_indices, get_Ms_and_Ds, get_bch_decoder
)


class TestQuery(unittest.TestCase):
    def setUp(self):
        # Common parameters
        self.n = 8
        self.b = 2
        self.q = 2

    def test_get_Ms_simple(self):
        # Test basic functionality
        Ms = get_Ms_simple(self.n, self.b, num_to_get=3)

        # Check type and length
        self.assertIsInstance(Ms, list)
        self.assertEqual(len(Ms), 3)

        # Check each matrix properties
        for M in Ms:
            self.assertIsInstance(M, np.ndarray)
            self.assertEqual(M.shape, (self.n, self.b))
            self.assertTrue(np.all((M == 0) | (M == 1)))

        # Check specific structure - identity blocks
        M0 = Ms[0]

        # Test with different parameters
        Ms = get_Ms_simple(10, 3, num_to_get=2)
        self.assertEqual(len(Ms), 2)
        self.assertEqual(Ms[0].shape, (10, 3))

    def test_get_Ms_complex(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Test basic functionality
        Ms = get_Ms_complex(self.n, self.b, self.q, num_to_get=2)

        # Check type and length
        self.assertIsInstance(Ms, list)
        self.assertEqual(len(Ms), 2)

        # Check each matrix properties
        for M in Ms:
            self.assertIsInstance(M, np.ndarray)
            self.assertEqual(M.shape, (self.n, self.b))
            self.assertTrue(np.all((M >= 0) & (M < self.q)))

    def test_get_Ms_parity(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Test basic functionality
        Ms = get_Ms_parity(self.n, self.b, self.q, num_to_get=2)

        # Check type and length
        self.assertIsInstance(Ms, list)
        self.assertEqual(len(Ms), 2)

        # Check each matrix properties
        for M in Ms:
            self.assertIsInstance(M, np.ndarray)
            self.assertEqual(M.shape, (self.n, self.b))
            self.assertTrue(np.all(M[:, 0] == 1))  # First column should be all ones
            self.assertTrue(np.all((M >= 0) & (M < self.q)))

    def test_get_Ms_antithetic(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Test basic functionality with b >= 2
        b = 3
        Ms = get_Ms_antithetic(self.n, b, self.q, num_to_get=2)

        # Check type and length
        self.assertIsInstance(Ms, list)
        self.assertEqual(len(Ms), 2)

        # Check each matrix properties
        for M in Ms:
            self.assertIsInstance(M, np.ndarray)
            self.assertEqual(M.shape, (self.n, b))

            # Check relationship between first column and original first column
            for i in range(self.n):
                self.assertEqual(M[i, 0] + M[i, 1], 1)

    def test_get_Ms_complex_low_degree(self):
        # Test basic functionality
        Ms = get_Ms_complex_low_degree(self.n, self.b, self.q, num_to_get=2)

        # Check type and length
        self.assertIsInstance(Ms, list)
        self.assertEqual(len(Ms), 2)

        # Check each matrix properties
        for M in Ms:
            self.assertIsInstance(M, np.ndarray)
            self.assertEqual(M.shape, (self.n, self.b))
            self.assertTrue(np.all((M == 0) | (M == 1)))

    def test_get_Ms(self):
        # Test different methods
        methods = ["simple", "complex", "complex_ld", "parity", "antithetic"]

        for method in methods:
            Ms = get_Ms(self.n, self.b, self.q, method=method, num_to_get=2)

            # Check type and length
            self.assertIsInstance(Ms, list)
            self.assertEqual(len(Ms), 2)

            # Check each matrix properties
            for M in Ms:
                self.assertIsInstance(M, np.ndarray)
                self.assertEqual(M.shape, (self.n, self.b))

        # Test error condition
        with self.assertRaises(ValueError):
            get_Ms(self.n, self.b, self.q, method="simple", num_to_get=self.n)

    def test_get_D_identity(self):
        # Test basic functionality
        D = get_D_identity(self.n)

        # Check type and shape
        self.assertIsInstance(D, np.ndarray)
        self.assertEqual(D.shape, (self.n + 1, self.n))

        # Check content - first row all zeros, then identity matrix
        self.assertTrue(np.all(D[0] == 0))
        self.assertTrue(np.array_equal(D[1:], np.eye(self.n)))

    def test_get_D_random(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Test basic functionality
        num_delays = 5
        D = get_D_random(self.n, q=self.q, num_delays=num_delays)

        # Check type and shape
        self.assertIsInstance(D, np.ndarray)
        self.assertEqual(D.shape, (num_delays, self.n))

        # Check content - all values in range [0, q-1]
        self.assertTrue(np.all((D >= 0) & (D < self.q)))

    def test_get_D_joint_coded(self):
        # Test basic functionality
        t = 2  # Error correction parameter
        D = get_D_joint_coded(self.n, t=t)

        # Check type
        self.assertIsInstance(D, np.ndarray)

        # Check content - all values are binary (0 or 1)
        self.assertTrue(np.all((D == 0) | (D == 1)))

    def test_get_D_channel_identity(self):
        # Test basic functionality
        D = np.array([[0, 1], [1, 0]])
        result = get_D_channel_identity(2, D, q=self.q)

        # Check type and content
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertTrue(np.array_equal(result[0], D % self.q))

    def test_get_D_nso(self):
        # Set random seed for reproducibility
        np.random.seed(42)

        # Test basic functionality
        D_source = np.array([[0, 1], [1, 0]])
        num_repeat = 3
        result = get_D_nso(2, D_source, q=self.q, num_repeat=num_repeat)

        # Check type and shape
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), num_repeat)

        # Each element should be a row with modulated offsets
        for row in result:
            self.assertEqual(row.shape, (2, 2))

    def test_get_D(self):
        # Test identity source with identity channel
        D = get_D(self.n, delays_method_source="identity", delays_method_channel="identity")
        self.assertIsInstance(D, list)
        self.assertEqual(len(D), 1)

        # Test random source with identity channel
        D = get_D(self.n, delays_method_source="random", delays_method_channel="identity",
                  q=self.q, num_delays=3)
        self.assertIsInstance(D, list)
        self.assertEqual(len(D), 1)

        # Test with nso channel
        D = get_D(self.n, delays_method_source="identity", delays_method_channel="nso",
                  q=self.q, num_repeat=2)
        self.assertIsInstance(D, list)
        self.assertEqual(len(D), 2)

    def test_subsample_indices(self):
        # Test with a specific matrix and delay
        M = np.array([[1, 0], [0, 1]], dtype=int)
        d = np.array([0, 0], dtype=int)
        indices = subsample_indices(M, d)

        # Check type and content
        self.assertIsInstance(indices, np.ndarray)
        self.assertEqual(len(indices), 2 ** M.shape[1])
        self.assertTrue(np.all(indices >= 0))
        self.assertTrue(np.all(indices < 2 ** M.shape[0]))

        # Test with different delay
        d = np.array([1, 0], dtype=int)
        indices = subsample_indices(M, d)
        self.assertEqual(len(indices), 2 ** M.shape[1])

    def test_get_Ms_and_Ds(self):
        # Test basic functionality
        Ms, Ds = get_Ms_and_Ds(self.n, self.q, query_method="simple", b=self.b,
                               num_subsample=3, delays_method_source="identity")

        # Check types and lengths
        self.assertIsInstance(Ms, list)
        self.assertIsInstance(Ds, list)
        self.assertEqual(len(Ms), 3)
        self.assertEqual(len(Ds), 3)

    def test_get_bch_decoder(self):
        # Test hard decoder
        n = 15
        t = 2
        decoder = get_bch_decoder(n, t, dectype="hard")
        self.assertTrue(callable(decoder))

        # Test soft decoder
        decoder = get_bch_decoder(n, t, dectype="soft", chase_depth=2)
        self.assertTrue(callable(decoder))

        # Test soft-list decoder
        decoder = get_bch_decoder(n, t, dectype="soft-list", chase_depth=2)
        self.assertTrue(callable(decoder))

        # Test invalid decoder type
        with self.assertRaises(NotImplementedError):
            get_bch_decoder(n, t, dectype="invalid")


if __name__ == '__main__':
    unittest.main()