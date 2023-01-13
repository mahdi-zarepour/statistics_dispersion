"""
Range
"""
import numpy as np


class Range:
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.calculate_range()
    
    def data_checker(self, data):
        if isinstance(data, list):
            return True
        else:
            raise ValueError('data must be a list and contains numbers')

    def calculate_range(self):
        self.min = np.min(self.data)
        self.max = np.max(self.data)
        return self.max - self.min


__all__ = [
    'Range',
]
