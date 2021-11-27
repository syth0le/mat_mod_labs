from lab_4.math_utils import *


# Возвращаем выборку и интервал
def create_normal_sampling(a, b):
    if a > b:
        print("Данные некорректны")
        raise SystemExit(1)
    r = generate_random_variables(1000)
    x = []
    for i in r:
        xr = reverse_fun(i, a, b)
        x.append(xr)
    x = quicksort(x)
    interval = [a, b]
    return x, interval


def create_gauss_sampling(m, d):
    sigma = math.sqrt(d)
    n = 6
    x = []
    for i in range(1000):
        v = 0
        for j in range(n):
            v += rnd.random()
        xi = fun_gauss(v, m, sigma, n)
        x.append(xi)
    x = quicksort(x)
    # Интервал от минимального до максимального x
    interval = [x[0], x[-1]]
    return x, interval


def create_rayleigh_sampling(sigma):
    # Легко убедиться, что максимальное значение приобретает функция если аргумент xl равен sigma
    max_y = rayleigh_distribution(sigma, sigma)
    ri = generate_random_variables(3000)
    x = []
    i = 1
    while i < 3000:
        X = sigma * 4 * ri[i]
        Y = max_y * ri[i - 1]
        if Y <= rayleigh_distribution(X, sigma):
            x.append(X)
        i += 1
        if len(x) >= 1000:
            break
    x = quicksort(x)
    # Интервал от 0 до максимального X
    interval = [0, x[-1]]
    return x, interval
