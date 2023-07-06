#!/usr/bin/python3
"""Define add function

    Functions:
        add_integer(int, int)
"""


def add_integer(a, b=98):
    """adds 2 numbers to each other

       args:
            a(int): first number
            b(int: second number

        Return:
            addition of 2 numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
