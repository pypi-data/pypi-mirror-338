import unittest
import numpy as np
from dsef.line_tools import normalized, normalvector, calc_heading_vector, calc_heading, RunningExponentialVectorAverage

class TestLineTools(unittest.TestCase):
    
    def test_normalized(self) -> None:
        v = [3, 4]
        result = normalized(v)
        expected = np.array([0.6, 0.8])
        np.testing.assert_almost_equal(result, expected)
    
    def test_normalized_zero_vector(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            normalized([0, 0])
    
    def test_normalvector_ccw(self) -> None:
        v = [1, 0]
        result = normalvector(v, CC=True, NORMALIZE=True)
        expected = np.array([0, -1])
        np.testing.assert_almost_equal(result, expected)
    
    def test_normalvector_cw(self) -> None:
        v = [1, 0]
        result = normalvector(v, CC=False, NORMALIZE=True)
        expected = np.array([0, 1])
        np.testing.assert_almost_equal(result, expected)
    
    def test_calc_heading_vector(self) -> None:
        result = calc_heading_vector(90)
        expected = np.array([1, 0])
        np.testing.assert_almost_equal(result, expected)
    
    def test_calc_heading_vector_invalid(self):
        with self.assertRaises(TypeError):
            calc_heading_vector("ninety")
    
    def test_calc_heading(self) -> None:
        heading_vec = (1, 0)
        result = calc_heading(heading_vec)
        expected = 90.0
        self.assertAlmostEqual(result, expected)
    
    def test_calc_heading_invalid(self) -> None:
        with self.assertRaises(TypeError):
            calc_heading("invalid_vector")
    
    def test_reva_initialization(self) -> None:
        reva = RunningExponentialVectorAverage()
        np.testing.assert_almost_equal(reva.mu, np.array([0, 0]))
        np.testing.assert_almost_equal(reva.var, np.array([0, 0]))
        self.assertEqual(reva.rho, 0.1)
    
    def test_reva_push(self) -> None:
        reva = RunningExponentialVectorAverage()
        reva.push(np.array([1.0, 1.0]))
        expected_mu = np.array([0.1, 0.1])
        np.testing.assert_almost_equal(reva.mu, expected_mu)
    
    def test_reva_push_invalid(self) -> None:
        reva = RunningExponentialVectorAverage()
        with self.assertRaises(TypeError):
            reva.push("invalid_vector")

if __name__ == "__main__":
    unittest.main()