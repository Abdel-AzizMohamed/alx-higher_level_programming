#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    for row in matrix:
        for count, column in enumerate(row):
            if count + 1 == len(row):
                print("{:d}".format(column))
            else:
                print("{:d}".format(column), end=" ")
