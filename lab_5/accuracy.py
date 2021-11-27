import numpy as np

from integration import Analytical, Trapezium


class Accuracy:

    @staticmethod
    def count_trapezium_method_accuracy(n):
        result = Trapezium.count(2 * n) - Trapezium.count(n)
        return result

    @staticmethod
    def investigate_num_of_nodes_to_1_percent_accuracy(func):
        expected_accuracy = np.abs(Analytical.count() / 100)
        i = 100
        n = 1
        temp = np.abs(func(n))
        while i > expected_accuracy:
            n *= 2
            i = np.abs(func(n) - temp)
            # print(temp, func(n), i)
            temp = np.abs(func(n))
        #     # print(temp, func(n), i)
        # print('\n')
        return n
