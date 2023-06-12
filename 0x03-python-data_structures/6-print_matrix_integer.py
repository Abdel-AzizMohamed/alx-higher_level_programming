#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    for row in matrix:
        for count, column in enumerate(row):
            if count + 1 == len(row):
                print("{:d}".format(column))
            else:
                print("{:d}".format(column), end=" ")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
