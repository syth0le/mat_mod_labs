import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
from abc import ABCMeta, abstractmethod

from utils.sorting import bubble_sort


class ABSMethods(metaclass=ABCMeta):
    def __init__(self, function):
        self.function = function

    @abstractmethod
    def drawGraphic(self, vectors):
        pass

class Lagranz(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, xl):
        z = 0
        for j in range(len(y)):
            p1 = 1
            p2 = 1
            for i in range(len(x)):
                if i == j:
                    p1 = p1 * 1
                    p2 = p2 * 1
                else:
                    p1 = p1 * (xl - x[i])
                    p2 = p2 * (x[j] - x[i])
            z = z + y[j] * p1 / p2
        return z

    def drawGraphic(self, vectors):

        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            xl = np.linspace(np.min(x), np.max(x))
            yl = self.counter(x, y, xl)
            plt.scatter(x, y)
            plt.plot(xl, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Lagranz Method")
        plt.show()


class InterpolationLinear(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, xl):
        yx = 0
        for i in range(len(x)):
            if x[i - 1] <= xl <= x[i]:
                yp = y[i] - y[i - 1]
                xp = x[i] - x[i - 1]
                yx = y[i] + ((yp / xp) * (xl - x[i]))
                break
        return yx

    def drawGraphic(self, vectors):

        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            yl = [self.counter(x, y, i) for i in x]
            plt.scatter(x, y)
            plt.plot(x, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Piecewise linear interpolation Method")
        plt.show()


class InterpolationParabolic(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y, arg, i ):
        y0 = y[i]
        y1 = y[i + 1]
        y2 = y[i + 2]
        x0 = x[i]
        x1 = x[i + 1]
        x2 = x[i + 2]
        return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * \
               (((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)))

    def counter2(self, x, y):
        a0 = []
        a1 = []
        a2 = []
        for i in range(1, len(x) - 1):
            a2.append(((y[i + 1] - y[i - 1]) / ((x[i + 1] - x[i - 1]) * (x[i + 1] - x[i]))) - (
                        (y[i] - y[i - 1]) / ((x[i] - x[i - 1]) * (x[i + 1] - x[i]))))
            a1.append((y[i] - y[i - 1] - (a2[i - 1] * ((x[i] ** 2) - (x[i - 1] ** 2)))) / (x[i] - x[i - 1]))
            a0.append(y[i - 1] - (a1[i - 1] * x[i - 1]) - (a2[i - 1] * (x[i - 1] ** 2)))

        return a0, a1, a2

    def drawGraphic(self, vectors):
        colors = plt.rcParams["axes.prop_cycle"]()
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            # a0, a1, a2 = self.counter(x, y)
            # for i in range(0, len(x) - 2, 2):
            #     xi = np.linspace(x[i], x[i + 2])
            #     f = a0[i] + a1[i] * xi + a2[i] * xi * xi
            #     plt.plot(xi, f)
            # plt.scatter(x, y)
            c = next(colors)["color"]
            if len(x) == 3:
                xl = np.linspace(np.min(x), np.max(x))
                yl = [self.counter(x, y, arg, 0) for arg in xl]
                plt.plot(xl, yl, color=c)
                # Проходимся по каждой паре точек
            for i in range(0, len(x) - 2, 2):
                xl = np.linspace(x[i], x[i + 2])
                yl = [self.counter(x, y, arg, i) for arg in xl]
                plt.plot(xl, yl, color=c)
            plt.scatter(x, y, color=c)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Piecewise parabolic interpolation Method")
        plt.show()


class InterpolationSpline(ABSMethods):

    def __call__(self, *args, **kwargs):
        call = self.function()
        self.drawGraphic(call)
        return call

    def counter(self, x, y):
        tck = interpolate.splrep(x, y, s=0)
        xl = np.linspace(np.min(x), np.max(x))
        yl = interpolate.splev(xl, tck, der=0)
        return xl, yl

    def drawGraphic(self, vectors):
        for vector in vectors:
            vector = bubble_sort(vector)
            x = vector[0]
            y = vector[1]
            xl, yl = self.counter(x, y)
            plt.scatter(x, y)
            plt.plot(xl, yl)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Spline interpolation Method")
        plt.show()


class Graphics(ABSMethods):

    def __call__(self, *args, **kwargs):
        # call = self.function()
        # print(call)
        call = 0
        self.drawGraphic(call)
        return call

    def drawGraphic(self, call):
        print("\n1 - Lagranz\n2 - Linear\n3 - Parabolic\n4 - Spline")
        command = int(input("Введите номер задания (из методички):"))
        if command == 1:
            meth = Lagranz(self.function)
            meth()
        elif command == 2:
            meth = InterpolationLinear(self.function)
            meth()
        elif command == 3:
            meth = InterpolationParabolic(self.function)
            meth()
        elif command == 4:
            meth = InterpolationSpline(self.function)
            meth()
        else:
            print("Invalid command")

