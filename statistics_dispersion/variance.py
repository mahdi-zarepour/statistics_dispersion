"""
Variance
"""
import numpy as np

from .data_checker import DataChecker


class Variance(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.var()

    def var(self):
        return np.var(self.data)


__all__ = [
    'Variance',
]
