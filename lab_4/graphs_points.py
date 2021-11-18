import math


def create_histogram(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = int(1 + 3.21 * math.log2(N))  # число интервалов
    R = b - a  # Определяем размах выборки
    width_interval = R / k
    data_hist = []
    for i in range(k):
        # Определяем интервал. Определяем, сколько элементов входят в него
        x_min = a + width_interval * i
        x_max = a + width_interval * (i + 1)
        count_elements = 0
        for x in X:
            if x_min < x <= x_max:
                count_elements += 1
            # Массив отсортирован и если элемент выходит из интервала, то заканчиваем подсчет
            if x > x_max:
                break
        w = count_elements / (N * width_interval)
        data_hist.append([w, x_min, x_max])
    return data_hist, k


def create_polygon(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = int(1 + math.log2(N))  # число интервалов
    R = b - a  # Определяем размах выборки
    width_interval = R / k
    data_polygon = []
    for i in range(k):
        q = a + width_interval * (i + 1)
        kq = 0
        for x in X:
            if x < q:
                kq += 1
        f = kq / N
        data_polygon.append([f, q])
    return data_polygon, k

