#!/usr/bin/python3
"""Define a object lockup function

    Functions:
        lookup(object)
"""


def lookup(obj):
    """returns the list of attributes and methods of an object"""
    return dir(obj)
