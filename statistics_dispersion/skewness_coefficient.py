"""
Skewness Coefficient
"""
import numpy as np

from .data_checker import DataChecker


class SkewnessCoefficient(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers,
            this class only calculate pearson formula with median
        """
        self.data = data
        self.data_checker(self.data)

    def __call__(self):
        return self.sc()

    def sc(self):
        self.mean = np.mean(self.data)
        self.std = np.std(self.data)
        self.median = np.median(self.data)
        return 3 * (self.mean - self.median) / self.std


__all__ = [
    'SkewnessCoefficient',
]
