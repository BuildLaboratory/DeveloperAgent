import unittest

from mathtools.number_theory import gcd, is_even, is_prime, lcm


class TestNumberTheory(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 97]
        non_primes = [0, 1, 4, 9, 15, 25, 100]
        for n in primes:
            self.assertTrue(is_prime(n), n)
        for n in non_primes:
            self.assertFalse(is_prime(n), n)

    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(7, 13), 1)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
