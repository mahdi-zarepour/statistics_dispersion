"""
Range
"""
import numpy as np

from .data_checker import DataChecker


class Range(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.calculate_range()

    def calculate_range(self):
        self.min = np.min(self.data)
        self.max = np.max(self.data)
        return self.max - self.min


__all__ = [
    'Range',
]
