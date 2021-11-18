from lab_4.math_utils import *


def plot_histogram(X, data_hist, k, interval, title, dstr, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    delta = (b - a) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]  # частота
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.title(title)
    # Рисуем плотность распределения(Да, мне лень нормально называть)
    plot_density_fn(X, a, b, dstr, m, d, sigma)
    plt.show()


def plot_polygon(X, data_polygon, interval, title, dstr, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    plt.step(x, y)
    plt.title(title)
    # Рисуем функцию распределения(Да, мне лень нормально называть)
    plot_density_f(X, a, b, dstr, m, d, sigma)
    plt.show()


def plot_hist_polygon(data_polygon, data_hist, k, interval, title):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    delta = (b - a) / k
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]  # частота
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.step(x, y)
    plt.title(title)
    plt.show()
