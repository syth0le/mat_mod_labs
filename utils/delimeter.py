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
        a = input(f"Пример: 1-3 или 5. Для выбора всех графиков введите 0:\n")
        try:
            command = list(map(int, a.split('-')))
        except ValueError:
            command = list(map(int, a.split(' ')))
        return self.ranged(command=command, call=call)

    @index_catcher
    def ranged(self, command, call):
        temp = []
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
            for inx in command:
                temp.append(call[inx-1])
            return temp
