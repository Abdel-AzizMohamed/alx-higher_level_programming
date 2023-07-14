#!/usr/bin/python3
"""Define a file read function


    Functions:
        read_file
"""


def read_file(filename=""):
    """ This function read a file content
        and print it outin the stdout
    """
    with open(filename, "r", encoding="UTF-8") as r:
        print(r.read(), end="")
