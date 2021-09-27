from abc import ABCMeta, abstractmethod

import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame
import seaborn as sns


class ABSGraphics(metaclass=ABCMeta):

    def __init__(self, function):
        self.function = function

    @abstractmethod
    def drawGraphic(self, vectors):
        pass


class Pandas(ABSGraphics):
    # df.plot(kind='line')
    def drawGraphic(self, vectors):
        # filter_vectors = get_graphs(vectors)
        for vector in vectors:
            x = vector[0]
            y = vector[1]
            plt.scatter(x, y)
        plt.show()

    def __call__(self, *args, **kwargs):
        df = DataFrame(np.random.randn(10, 2), columns=['col1', 'col2'])
        # df.plot.scatter(x='col1', y='col2', s=120)
        df.plot(kind='scatter', x='col1', y='col2', s=120)
        plt.show()

        print(self.function(*args, **kwargs))
        return self.function


class Matplotlib(ABSGraphics):

    def drawGraphic(self, vectors):
        # filter_vectors = get_graphs(vectors)
        for vector in vectors:
            x = vector[0]
            y = vector[1]
            plt.scatter(x, y)
        plt.show()

    def __call__(self, *args, **kwargs):
        x = np.arange(0, 7, 0.25)
        y = np.cos(x)
        plt.scatter(x, y)
        # plt.plot(x, y)
        plt.show()

        print(self.function(*args, **kwargs))
        return self.function


class Seaborn(ABSGraphics):

    def drawGraphic(self, vectors):
        # filter_vectors = get_graphs(vectors)
        for vector in vectors:
            x = vector[0]
            y = vector[1]
            plt.scatter(x, y)
        plt.show()

    def __call__(self, *args, **kwargs):
        x = np.arange(0, 10.5, 0.5)
        y = np.cos(x)
        sns.lineplot(x, y)
        plt.show()
        # self.drawGraphic()

        print(self.function(*args, **kwargs))
        return self.function


class Graphics:

    def __init__(self, func, gr_class):
        self.func = func
        self.gr_class = gr_class

    def __call__(self, *args, **kwargs):
        # choose class of graphics
        # do initialization if class and do some work
        pass


if __name__ == "__main__":
    x = np.arange(0, 10.5, 0.5)

    y = np.cos(x)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()
