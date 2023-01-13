import unittest

from statistics_dispersion.standard_devaition import StandardDeviation


class TestStandardDeviation(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        self.st = StandardDeviation(self.data)

    def test_data_checker(self):
        self.assertTrue(self.st.data_checker(self.data))

    def test_calculate_st(self):
        self.assertEqual(self.st.st(), 2.8722813232690143299253057341095)
    
    def test_st_call_method(self):
        self.assertEqual(self.st(), 2.8722813232690143299253057341095)
