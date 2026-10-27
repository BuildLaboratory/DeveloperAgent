import math
import unittest

from mathtools.geometry import (
    circle_area,
    circle_circumference,
    rectangle_area,
    rectangle_perimeter,
    triangle_area,
)


class TestGeometry(unittest.TestCase):
    def test_rectangle(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_perimeter(3, 4), 14)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 5), 25)

    def test_circle(self):
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)
        self.assertAlmostEqual(circle_circumference(1), 2 * math.pi)


if __name__ == "__main__":
    unittest.main()
