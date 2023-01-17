import unittest

from statistics_dispersion.central_moment import CentralMoment


class TestCentralMoment(unittest.TestCase):
    def setUp(self):
        self.data = [32, 31, 39, 36, 38,]
        self.cm = CentralMoment(self.data, 3)

    def test_data_checker(self):
        self.assertTrue(self.data)

    def test_cm(self):
        self.assertEqual(self.cm.cm(), -5.904000000000086)

    def test_call_method(self):
        self.assertEqual(self.cm(), -5.904000000000086)
        