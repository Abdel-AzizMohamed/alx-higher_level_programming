#!/usr/bin/python3
"""Define a rectangle class

    Classes:
        Rectangle
"""


class Rectangle():
    """Define a Rectangle Object

        Methods:
            __init__(self, width=0, height=0)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Intalize a new object

            Args:
                width(int): object width
                height(int): object height
        """
        self.width = width
        self.height = height

    def __str__(self):
        for i in range(self.__height - 1):
            for j in range(self.__width):
                print("#", end="")
            print("")
        return "#" * self.__width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
