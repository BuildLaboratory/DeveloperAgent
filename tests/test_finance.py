import unittest

from mathtools.finance import (
    annuity_payment,
    break_even_units,
    compound_interest,
    simple_interest,
)


class TestFinance(unittest.TestCase):
    def test_simple_interest(self):
        self.assertAlmostEqual(simple_interest(1000, 5, 2), 100)

    def test_compound_interest(self):
        self.assertAlmostEqual(compound_interest(1000, 10, 2), 1210)

    def test_annuity_payment(self):
        self.assertAlmostEqual(annuity_payment(10000, 5, 10), 1295.05, places=2)
        self.assertAlmostEqual(annuity_payment(1200, 0, 12), 100)

    def test_break_even_units(self):
        self.assertEqual(break_even_units(1000, 15, 5), 100)

    def test_break_even_invalid(self):
        with self.assertRaises(ValueError):
            break_even_units(1000, 5, 5)


if __name__ == "__main__":
    unittest.main()
