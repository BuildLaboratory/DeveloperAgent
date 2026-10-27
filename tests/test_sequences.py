import unittest

from mathtools.sequences import factorial, fibonacci, sum_up_to


class TestSequences(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        for n, value in enumerate(expected):
            self.assertEqual(fibonacci(n), value)

    def test_sum_up_to(self):
        self.assertEqual(sum_up_to(0), 0)
        self.assertEqual(sum_up_to(10), 55)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
