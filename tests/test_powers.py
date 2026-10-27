import unittest

from mathtools.powers import cube, power, square, square_root


class TestPowers(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(-3), 9)

    def test_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(-2), -8)

    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(7, 0), 1)

    def test_power_negative_exponent(self):
        with self.assertRaises(ValueError):
            power(2, -1)

    def test_square_root(self):
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()
