"""
Central Moment
"""
import numpy as np

from .data_checker import DataChecker


class CentralMoment(DataChecker):
    def __init__(self, data:list, r:int):
        """
            data should be a list of numbers,
            r is your desire power for central moments 
        """
        self.data = data
        self.data_len = len(self.data)
        self.r = r
        self.data_checker(self.data)

    def __call__(self):
        return self.cm()

    def cm(self):
        sumation = 0
        mean = np.mean(self.data)
        for num in self.data:
            sumation += (num - mean) ** self.r
        
        return sumation / self.data_len


__all__ = [
    'CentralMoment',
]
