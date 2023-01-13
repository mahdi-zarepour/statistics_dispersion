"""
Standard Deviation
"""
import numpy as np

from .data_checker import DataChecker

class StandardDeviation(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.st()

    def st(self):
        return np.sqrt(np.var(self.data))


__all__ = [
    'StandardDeviation',
]
