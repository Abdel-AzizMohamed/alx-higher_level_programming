#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for i, row in enumerate(new_matrix):
        for j, column in enumerate(row):
            new_matrix[i][j] **= 2
    return new_matrix
