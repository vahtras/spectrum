import unittest
import gaussian

import math
SQRT_PI = math.sqrt(math.pi)

class NewTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single(self):
        center=0
        height=1
        width=.1
        g = gaussian.generate_gaussian(center, height, width)
        self.assertEqual(height, g(center))

    def test_double_peak(self):
        center1 = 0
        height1 = 1
        width1 = .1

        center2 = 1
        height2 = 1
        width2 = .1

        g = gaussian.generate_spectrum(
            (center1, height1, width1),
            (center2, height2, width2)
            )

        self.assertAlmostEqual(height1, g(center1))
        self.assertAlmostEqual(height2, g(center2))

    def test_single_shift(self):
        center=0
        height=1
        width=.1
        g = gaussian.generate_spectrum((center, height, width), shift=-1)
        self.assertEqual(height, g(center-1))

class NewTestA(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single(self):
        center=0
        area=1
        width=.1
        g = gaussian.generate_gaussian_area(center, area, width)
        self.assertEqual(area/(width*SQRT_PI), g(center))

    def test_double_peak(self):
        center1 = 0
        area1 = 1
        width1 = .1

        center2 = 1
        area2 = 1
        width2 = .1

        g = gaussian.generate_spectrum(
            (center1, area1, width1),
            (center2, area2, width2)
            )

        self.assertAlmostEqual(area1, g(center1))
        self.assertAlmostEqual(area2, g(center2))

    def test_single_shift(self):
        center=0
        area=1
        width=.1
        g = gaussian.generate_spectrum((center, area, width), shift=-1)
        self.assertEqual(area, g(center-1))


if __name__ == "__main__":
    unittest.main()
