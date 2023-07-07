#!/usr/bin/python3

"""Define matrix divied

   Functions:
        matrix_divided
"""


def matrix_divided(matrix, div):
    """Divied given matrix by a number

        Args:
            matrix (list): the given matrix
            div (int, float): divider
        Return:
            new matrix divided by div
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for column in row:
            if not isinstance(column, int) and not isinstance(column, float):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            if div == float("inf"):
                new_list.append(float("{:2f}".format(0)))
                continue
            elif div == float("-inf"):
                new_list.append(float("-{:2f}".format(0)))
                continue
            new_list.append(round(column / div, 2))

        new_matrix.append(new_list)
    return new_matrix
