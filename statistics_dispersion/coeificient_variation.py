"""
Coeificient of Variation
"""
import numpy as np

from .data_checker import DataChecker
from .standard_devaition import StandardDeviation


class CoeificientVariation(DataChecker):
    def __init__(self, data):
        """
            data should be a list of numbers
        """
        self.data = data
        self.data_checker(self.data)
    
    def __call__(self):
        return self.cv()

    def cv(self):
        self.mean = np.mean(self.data)
        self.std = StandardDeviation(self.data).st()
        self.cv = (self.std / self.mean) * 100
        return self.cv


__all__ = [
    'CoeificientVariation',
]
