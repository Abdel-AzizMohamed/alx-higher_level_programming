#!/usr/bin/python3
"""Define a is_kind_of_class function

    Functions:
        is_kind_of_class(object, class)
"""


def inherits_from(obj, a_class):
    """Define a function that checks if the object is instance
        from a given class

        Return: True if the object is instance else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
