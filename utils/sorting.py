def quick_sort(vector):
    length = len(vector[0])

    # print(vector)
    for i in range(length):
        for j in range(length-1):
            if vector[0][j] > vector[0][j+1]:
                vector[0][j], vector[0][j+1] = vector[0][j+1], vector[0][j]
                vector[1][j], vector[1][j+1] = vector[1][j+1], vector[1][j]

    # print(vector)
    return vector


if __name__ == "__main__":
    dots = [[3, 5, 6, 8, 1], [1, 2, 3, 7, 10]]
    quick_sort(dots)
