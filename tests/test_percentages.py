import unittest

from mathtools.percentages import add_vat, apply_discount, percent_change, percent_of


class TestPercentages(unittest.TestCase):
    def test_percent_of(self):
        self.assertEqual(percent_of(20, 50), 10)

    def test_percent_change(self):
        self.assertAlmostEqual(percent_change(100, 120), 20)
        self.assertAlmostEqual(percent_change(200, 150), -25)

    def test_apply_discount(self):
        self.assertAlmostEqual(apply_discount(80, 25), 60)

    def test_add_vat(self):
        self.assertAlmostEqual(add_vat(100), 119)
        self.assertAlmostEqual(add_vat(100, 7), 107)


if __name__ == "__main__":
    unittest.main()
