#!/usr/bin/python3
"""Define a base class"""


class Base():
    """Define a base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init a new object"""
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
