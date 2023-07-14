#!/usr/bin/python3
"""Define MyInt Class"""


class MyInt(int):
    """Define MyInt object"""
    def __eq__(self, obj):
        return self.real != obj

    def __ne__(self, obj):
        return self.real == obj
