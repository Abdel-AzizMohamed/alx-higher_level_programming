#!/usr/bin/python3
"""Define Empty classes

    Classes:
        BaseGeometry()
        Rectangle(BaseGeometry)
"""


class BaseGeometry():
    """Define BaseGeomatry Object"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Define Rectangle Object"""
    def __init__(self, width, height):
        """intalize a new rect object

            Args:
                width(positive int): rect width
                height(positive int): rect height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
