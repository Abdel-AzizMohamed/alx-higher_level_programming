#!/usr/bin/python3

"""define a square object"""


class Square():
    """Represent A Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new object

        Args:
            size (int): the size of square object
        """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
            return 0

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
