#!/usr/bin/python3

"""define a square object"""


class Square():
    """Represent A Square"""
    def __init__(self, size=0):
        """Initialize a new object

        Args:
            size (int): the size of square object
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
