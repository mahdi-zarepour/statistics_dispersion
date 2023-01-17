import unittest

from statistics_dispersion.mean_absolute_of_deviation import MeanAbsoluteDeviation


class TestMeanAbsoluteDeviation(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        self.ad = MeanAbsoluteDeviation(self.data)

    def test_data_checker(self):
        self.assertTrue(self.data)

    def test_ad(self):
        self.assertEqual(self.ad.ad(), 2.5)

    def test_call_method(self):
        self.assertEqual(self.ad(), 2.5)
        