#!/usr/bin/python3
"""Defines a Python class to hson function."""


class Student():
    """Define a student object

        Magic Methods:
            __init__(self, first_name, last_name, age)

        Methods:
            to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """intalize student object

            Args:
                first_name(string): student first name
                last_name(string): student last name
                age(int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student"""
        return self.__dict__
