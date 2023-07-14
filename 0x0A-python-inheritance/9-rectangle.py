#!/usr/bin/python3
"""Define Empty classes

    Classes:
        BaseGeometry()
        Rectangle(BaseGeometry)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define Rectangle Object"""
    def __init__(self, width, height):
        """intalize a new rect object

            Args:
                width(positive int): rect width
                height(positive int): rect height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
