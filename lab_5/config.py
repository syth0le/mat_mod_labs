import math


class Config:
    MIN = 1
    MAX = 5

    @staticmethod
    def our_function(x):
        return math.log(x, math.e) / x

    def __repr__(self):
        return 'ln(x)/x'
