"""
Standard Deviation
"""
import numpy as np


class StandardDeviation:
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.st()
    
    def data_checker(self, data):
        if isinstance(data, list):
            return True
        else:
            raise ValueError('data must be a list and contains numbers')

    def st(self):
        return np.sqrt(np.var(self.data))


__all__ = [
    'StandardDeviation',
]
