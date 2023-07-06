#!/usr/bin/python3
"""Define print square

    Functions:
        print_square
"""


def print_square(size):
    """
        prints out a square with given size

        Args:
            size(int): size of square

        Raises:
            TypeError: if size is not integer
            ValueError: size < 0

        Return: Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print("")
