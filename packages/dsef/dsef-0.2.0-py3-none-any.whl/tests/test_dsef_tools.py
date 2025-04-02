import unittest
import numpy as np
from scipy import stats
from dsef.dsef_tools import get_t_critical, calc_dof, calc_heading_vector, calc_heading, heading2rotM, epanechnikov1D, gen_epanechnikov2D_kernel, FlutDir, DsefFilters

class TestDsefTools(unittest.TestCase):

    def test_get_t_critical(self):
        self.assertAlmostEqual(get_t_critical(10, 0.001), stats.t.ppf(0.999, 10))
        self.assertAlmostEqual(get_t_critical(5, 0.05), stats.t.ppf(0.95, 5))

    def test_calc_dof(self):
        self.assertEqual(calc_dof(1.0, 1.0, 10), 18)
        self.assertEqual(calc_dof(2.0, 3.0, 10), 17)

    def test_calc_heading_vector(self):
        result = calc_heading_vector(90)
        np.testing.assert_almost_equal(result, [1, 0])

    def test_calc_heading(self):
        result = calc_heading([1, 0])
        self.assertEqual(result, 90)

    def test_heading2rotM(self):
        result = heading2rotM(90)
        np.testing.assert_almost_equal(result, [[0, 1], [-1, 0]])

    def test_epanechnikov1D(self):
        result = epanechnikov1D(0)
        self.assertEqual(result, 3/4)

    def test_gen_epanechnikov2D_kernel(self):
        result = gen_epanechnikov2D_kernel(2)
        self.assertEqual(result.shape, (5, 5))

    def test_FlutDir_init(self):
        flut = FlutDir(10)
        self.assertEqual(len(flut.thetas), 37)

    def test_FlutDir_set_item(self):
        flut = FlutDir(10)
        flut.set_item(30, "Test Item")
        self.assertEqual(flut.items[flut.index(30)], "Test Item")

    def test_FlutDir_set_span(self):
        flut = FlutDir(10)
        center, inds, thetas = flut.set_span(45, 90)
        self.assertEqual(center, 50)
        self.assertEqual(len(inds), 11)

    def test_FlutDir_wrap_angle(self):
        flut = FlutDir(10)
        self.assertEqual(flut.wrap_angle(190), -170)
        self.assertEqual(flut.wrap_angle(-190), 170)

    def test_FlutDir_index(self):
        flut = FlutDir(10)
        self.assertEqual(flut.index(30), 21)

    def test_FlutDir_get_nearest(self):
        flut = FlutDir(10)
        flut.set_item(30, "Test Item")
        nearest_angle, item, vec = flut.get_nearest(30)
        self.assertEqual(nearest_angle, 30)
        self.assertEqual(item, "Test Item")

    def test_DsefFilters_init(self):
        dsef = DsefFilters(45)
        self.assertEqual(dsef.radius, 15)
        self.assertEqual(dsef.N, 3)

    def test_DsefFilters_set_direction(self):
        dsef = DsefFilters(45)
        dsef.set_direction(90, 90)
        self.assertEqual(dsef.flut.center, 0)

    def test_DsefFilters_exception_set_span(self):
        dsef = DsefFilters(45)
        with self.assertRaises(OSError):
            dsef.flut.set_span(0, 360)

    def test_DsefFilters_invalid_input(self):
        with self.assertRaises(TypeError):
            calc_heading_vector("90")
        
    def test_invalid_heading_vector(self):
        with self.assertRaises(ValueError):
            calc_heading("invalid_vector")

    def test_invalid_2d_kernel(self):
        with self.assertRaises(TypeError):
            gen_epanechnikov2D_kernel("string_radius")

if __name__ == '__main__':
    unittest.main()
