"""
Mean Absolute of Deviation
"""
import numpy as np

from .data_checker import DataChecker


class MeanAbsoluteDeviation(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_len = len(self.data)
        self.data_checker(self.data)

    def __call__(self):
        return self.ad()

    def mean(self):
        mean = np.mean(self.data)
        return mean

    def ad(self):
        abs_sumation = 0
        mean = self.mean()
        for num in self.data:
            abs_sumation += abs(num - mean)

        return abs_sumation / self.data_len
    

__all__ = [
    'MeanAbsoluteDeviation',
]
