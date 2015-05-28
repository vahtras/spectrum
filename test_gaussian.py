import unittest
import gaussian


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


if __name__ == "__main__":
    unittest.main()
