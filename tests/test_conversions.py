import unittest

from mathtools.conversions import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    miles_to_km,
)


class TestConversions(unittest.TestCase):
    def test_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_distance(self):
        self.assertAlmostEqual(miles_to_km(1), 1.609344)
        self.assertAlmostEqual(km_to_miles(1.609344), 1)


if __name__ == "__main__":
    unittest.main()
