import unittest

from mathtools.stats import maximum, mean, median, minimum, value_range


class TestStats(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_median_odd(self):
        self.assertEqual(median([5, 1, 3]), 3)

    def test_median_even(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_minimum_maximum(self):
        self.assertEqual(minimum([4, -2, 7]), -2)
        self.assertEqual(maximum([4, -2, 7]), 7)

    def test_value_range(self):
        self.assertEqual(value_range([4, -2, 7]), 9)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean([])


if __name__ == "__main__":
    unittest.main()
