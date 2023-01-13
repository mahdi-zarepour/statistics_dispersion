"""
Base class for all classes
"""
from abc import ABC


class DataChecker(ABC):
    def data_checker(self, data):
        if isinstance(data, list):
            return True
        else:
            raise ValueError('data must be a list and contains numbers')
