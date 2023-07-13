#!/usr/bin/python3
"""Define a is_same_class function

    Functions:
        is_same_class(object, class)
"""


def is_same_class(obj, a_class):
    """Define a function that checks if the object is instance
        from a given class

        Return: True if the object is instance else False
    """
    if type(obj) == a_class:
        return True
    return False
