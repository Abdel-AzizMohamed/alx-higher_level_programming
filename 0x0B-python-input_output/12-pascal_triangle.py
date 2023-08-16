#!/usr/bin/python3
"""Define a pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascals triangle"""
    pas_list = []

    if n <= 0:
        return []

    pas_list.append([1])

    for i in range(n - 1):
        row_list = []
        for j in range(i+2):
            if j == 0:
                row_list.append(1)
            elif j == i + 1:
                row_list.append(1)
            else:
                row_list.append(pas_list[i][j] + pas_list[i][j - 1])
        pas_list.append(row_list)
    return pas_list
