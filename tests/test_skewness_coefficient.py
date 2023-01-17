import unittest

from statistics_dispersion.skewness_coefficient import SkewnessCoefficient


class TestCoeificientVariation(unittest.TestCase):
    def setUp(self):
        self.data = [8, 5, 3, 6, 8, 8, 10, 19, 16, 30,]
        self.sc = SkewnessCoefficient(self.data)

    def test_data_checker(self):
        self.assertTrue(self.data)

    def test_sc(self):
        self.assertEqual(self.sc.sc(), 1.2758537104946477)

    def test_call_method(self):
        self.assertEqual(self.sc(), 1.2758537104946477)
