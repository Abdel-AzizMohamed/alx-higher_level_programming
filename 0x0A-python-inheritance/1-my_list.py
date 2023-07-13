#!/usr/bin/python3
"""
    Define a class

    Classes:
        MyList
"""


class MyList(list):
    """Define a subclass for list class

        Methods:
            print_sorted()
    """
    def print_sorted(self):
        """prints out a sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
