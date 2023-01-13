import unittest

from statistics_dispersion.variance import Variance


class TestVariance(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        self.var = Variance(self.data)

    def test_data_checker(self):
        self.assertTrue(self.var.data_checker(self.data))

    def test_var(self):
        self.assertEqual(self.var.var(), 8.25)
