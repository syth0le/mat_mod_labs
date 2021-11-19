import numpy as np
from matplotlib import pyplot as plt

from config import Config


def drawGraphic():
    a, b, func = Config.MIN, Config.MAX, Config.our_function
    x = np.linspace(a, b, 100)
    plt.plot(x, func(x))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graphic {Config()}')
    plt.show()
