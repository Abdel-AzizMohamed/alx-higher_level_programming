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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
