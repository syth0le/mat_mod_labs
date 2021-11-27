import numpy as np

from integration import Analytical, Trapezium


class Accuracy:

    @staticmethod
    def count_trapezium_method_accuracy(n):
        result = Trapezium.count(2 * n) - Trapezium.count(n)
        return result

    @staticmethod
    def investigate_num_of_nodes_to_1_percent_accuracy(func):
        expected_value = np.abs(Analytical.count())
        i = 100
        N = 1
        temp = np.abs(func(N))
        while i > 1:
            N *= 2
            i = np.abs(np.abs(func(N)) - temp) * 100 / expected_value
            temp = np.abs(func(N))
        return N
