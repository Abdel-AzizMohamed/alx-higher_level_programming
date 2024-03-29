#!/usr/bin/python3
"""Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Define a new rect object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init a new rect object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the object"""
        return self.__width * self.__height

    def display(self):
        """display the object by # sign"""
        for i in range(self.__y):
            print("")

        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """return string representation"""
        wd = self.__width
        hi = self.__height
        x = self.__x
        y = self.__y
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}"

        return str_rep.format(self.id, x, y, wd, hi)

    def update(self, *args, **kwargs):
        """update object attributes"""
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return (0)

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

    def to_dictionary(self):
        """create a dictionary repr of rect object"""
        new_dict = {"id": self.id, "width": self.__width,
                    "height": self.__height, "x": self.__x, "y": self.__y}
        return new_dict
