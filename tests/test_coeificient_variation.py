import unittest

from statistics_dispersion.coeificient_variation import CoeificientVariation


class TestCoeificientVariation(unittest.TestCase):
    def setUp(self):
        self.data = [58, 54, 82, 73, 67]
        self.cv = CoeificientVariation(self.data)

    def test_data_checker(self):
        self.assertTrue(self.data)

    def test_cv(self):
        self.assertEqual(self.cv.cv(), 15.130872776638654)

    def test_call_method(self):
        self.assertEqual(self.cv(), 15.130872776638654)
