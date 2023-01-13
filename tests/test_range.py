import unittest

from statistics_dispersion.range import Range


class TestRange(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        self.range = Range(self.data)

    def test_data_checker(self):
        self.assertTrue(self.range.data_checker(self.data))

    def test_calculate_range(self):
        self.assertEqual(self.range.calculate_range(), 9)
    
    def test_range_call_method(self):
        self.assertEqual(self.range(), 9)
