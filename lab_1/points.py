# написать через классы + написать класс что файлдескриптор делает с доставанием всех точек с файлов 
# + (написать декораторы для разных видов файлов (txt, xls....)
# + или сделать это через цепочку зависимостей классов для разных файлов какую нибудь)

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# можно написать поддекораторы для графиков и разных либ
# ( декорируют функцию что вычисляет точки, а график строится на основы либы и декоратора) -- это ваще круто пилотаж





@pandas_grЯя
@plotly_gr
@seaborn_gr
@matplotlib_gr
def plotter_scrabber(dots):
    # some work
    return dots[0], dots[1]


def matplotlib_gr(func):
    def wrapper(*args, **kwargs):
        rez = func()
        plt = PLOT()
        plt.plot(rez)
        plt.show()
        return rez
    return wrapper


или класс какой нить
class Matplot_Gen():
    
    def __init__(self, func):
        self.func = func
    
    def __call__(self, func)
        rez = func()
        plt = PLOT()
        plt.plot(rez)
        plt.show()
        return rez