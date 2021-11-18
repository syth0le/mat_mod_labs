import math
import random as rnd
import matplotlib.pyplot as plt


def reverse_fun(ri, ai, bi):
    return (ri * (bi - ai)) + ai


def rayleigh_distribution(xl, sigma):
    return (xl / (sigma ** 2)) * math.exp(-1 * ((xl ** 2) / (2 * (sigma ** 2))))


def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(rnd.random())
    return r


def fun_gauss(v, m, sigma, N):
    el = math.sqrt(12 / N) * (v - (N / 2))
    return sigma * el + m


def fn_normal(a, b, x):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


def f_normal(a, b, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0


def fn_gauss(x, m, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 * (x - m) ** 2 / (2 * (sigma ** 2)))


def f_gauss(x, m, sigma):
    return (1 / 2) * (1 + math.erf((x - m) / math.sqrt(2 * (sigma ** 2))))


def fn_rayleigh(x, sigma):
    return (x / (sigma ** 2)) * math.exp(-1 * ((x ** 2) / (2 * (sigma ** 2))))


def f_rayleigh(x, sigma):
    return 1 - math.exp(-1 * (x ** 2) / (2 * sigma ** 2))


def plot_density_fn(X, a, b, dstr, m=0, d=0, sigma=0):
    if dstr == 1:
        r = []
        for x in X:
            r.append(fn_normal(a, b, x))
        plt.plot(X, r)
    elif dstr == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(fn_gauss(x, m, sigma))
        plt.plot(X, r)
    elif dstr == 3:
        r = []
        for x in X:
            r.append(fn_rayleigh(x, sigma))
        plt.plot(X, r)


def plot_density_f(X, a, b, dstr, m=0, d=0, sigma=0):
    if dstr == 1:
        r = []
        for x in X:
            r.append(f_normal(a, b, x))
        plt.plot(X, r)
    elif dstr == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(f_gauss(x, m, sigma))
        plt.plot(X, r)
    elif dstr == 3:
        r = []
        for x in X:
            r.append(f_rayleigh(x, sigma))
        plt.plot(X, r)


def quicksort(array):
    if len(array) <= 1:  # Базовый случай
        return array
    else:  # Рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)
