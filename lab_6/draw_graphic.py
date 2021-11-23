import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def drawGraphic(a, b, func):
    x = np.linspace(a, b, 10000)
    sns.set_theme(style="darkgrid")
    sns.lineplot(x, func(x))
    plt.show()
