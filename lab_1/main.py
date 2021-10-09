from lab_1.files_chain import FilesChain
from lab_1.graphics import Matplotlib, Seaborn, Pandas


def index_catcher(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except:
            return []
    return wrapper


class Delimeter:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        call = self.function()
        print(f"Количество графиков в исходно выражении {len(call)} Выберите нужный диапазон или определнный график\n")
        command = list(map(int, input(f"Пример: 1-3 или 5. Для выбора всех графиков введите 0:\n").split('-')))
        return self.ranged(command=command, call=call)

    @index_catcher
    def ranged(self, command, call):
        if len(command) == 1:
            return call if command[0] == 0 else [call[command[0]-1]]

        elif len(command) == 2:
            # write handler for catching errors
            min_gr = command[0]-1
            max_gr = command[1]
            if min_gr < 0 or max_gr > len(call):
                return []
            return call[min_gr: max_gr]
        else:
            return "Range Error"


@Pandas
@Seaborn
@Matplotlib
@Delimeter
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()
