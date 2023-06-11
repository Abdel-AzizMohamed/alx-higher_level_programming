#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for count, column in enumerate(row):
            if count + 1 == len(row):
                print("{:d}".format(column))
            else:
                print("{:d}".format(column), end=" ")            
