import unittest

from mathtools.vectors import add_vectors, dot_product, scale_vector, vector_length


class TestVectors(unittest.TestCase):
    def test_add_vectors(self):
        self.assertEqual(add_vectors([1, 2], [3, 4]), [4, 6])

    def test_scale_vector(self):
        self.assertEqual(scale_vector([1, -2, 3], 2), [2, -4, 6])

    def test_dot_product(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_vector_length(self):
        self.assertAlmostEqual(vector_length([3, 4]), 5)

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            add_vectors([1, 2], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
