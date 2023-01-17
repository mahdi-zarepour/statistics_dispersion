"""
MedianAbsoluteDeviation
"""
import numpy as np

from .mean_absolute_of_deviation import MeanAbsoluteDeviation


class MedianAbsoluteDeviation(MeanAbsoluteDeviation):
    def ad(self):
        abs_sumation = 0
        median = np.median(self.data)
        for num in self.data:
            abs_sumation += abs(num - median)

        return abs_sumation / self.data_len


__all__ = [
    'MedianAbsoluteDeviation',
]
