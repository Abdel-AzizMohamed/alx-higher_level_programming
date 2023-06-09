#!/usr/bin/python3

"""Define a magic class"""

import math


class MagicClass():
    """Define a new MagicClass Object"""
    def __init__(self, radius=0):
        """Initalize a new object

        Args:
            radius (int, float): radius of the object
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Gets the area of the Object"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Gets the circumference of the Object"""
        return (2 * math.pi * self.__radius)
