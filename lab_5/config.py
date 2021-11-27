import numpy as np


class Config:
    MIN = 1
    # MIN = 0.5
    MAX = 5

    @staticmethod
    def our_function(x):
        return np.log(x) / x

    def __repr__(self):
        return 'ln(x)/x'
