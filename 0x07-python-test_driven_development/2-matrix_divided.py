#!/usr/bin/python3

"""Define matrix divied"""


import doctest


def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            new_list = []
            if not isinstance(column, int) and not isinstance(column, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(column / div, 3))

        new_matrix.append(new_list)
    return new_matrix

if __name__ == "__main__":
    #doctest.testfile("tests/2-matrix_divided.txt")
    matrix = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
