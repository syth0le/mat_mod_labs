import random

import numpy as np
from matplotlib import pyplot as plt
from numpy import std
from scipy import integrate


class Config:
    MIN = 0.5
    MAX = 5

    @staticmethod
    def our_function(x):
        return np.log(x) / x

    def __repr__(self):
        return 'ln(x)/x'


def drawGraphic():
    y = lambda x: Config.our_function(x)
    x = np.linspace(Config.MIN, Config.MAX, 150)
    plt.plot(x, y(x))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graphic {Config()}')
    plt.show()


def count_analytically():
    return integrate.quad(Config.our_function, Config.MIN, Config.MAX)


def count_trapezium_method(n):
    a = Config.MIN
    b = Config.MAX
    func = Config.our_function
    h = (b - a) / n
    s = 0
    while round(a, 8) < b:
        s += 0.5 * h * (func(a) + func(a + h))
        a += h
    return s


def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(random.random())
    return r


def count_trapezium_method_accuracy(n):
    result = count_trapezium_method(2 * n) - count_trapezium_method(n)
    return result


def investigate_num_of_nodes_to_1_percent_accuracy():
    expected_accuracy = 0.01
    i = 100
    n = 1
    temp = count_trapezium_method(n)
    while i > expected_accuracy:
        n *= 2
        i = count_trapezium_method(n) - temp
        temp = count_trapezium_method(n)

    return f'Result: {temp} number of separations: {n}, difference: {i}'


def count_monte_carlo_method_first(n=1000, N=100):
    # generate_random_variables(3000)
    s = 0
    I_values = []
    k_values = []
    for k in range(1, n + 1):
        x = random.uniform(Config.MIN, Config.MAX)
        s += Config.our_function(x)
        if (k % N) == 0:
            I = (float(Config.MAX - Config.MIN) / k) * s
            # print(I)
            I_values.append(I)
            k_values.append(k)
    return k_values, I_values


def count_monte_carlo_method_second():
    pass


if __name__ == '__main__':
    # drawGraphic()
    print(f'Analytic count: {count_analytically()[0]}')
    print()
    print(f'Trapezium method count: {count_trapezium_method(128)}')
    # print(f'Trapezium method accuracy: {count_trapezium_method_accuracy(128)}')
    print(investigate_num_of_nodes_to_1_percent_accuracy())
    print()
    print(f'Monte-Carlo 1st method count: {count_monte_carlo_method_first()}')
    print(f'Monte-Carlo 2nd method count: {count_monte_carlo_method_first()}')
    print()
    print(f'Count standard deviation for 1st method: {std(count_monte_carlo_method_first()[1])}')
    # print(f'Count standard deviation for 2nd method: {std(count_monte_carlo_method_second()[1])}')
