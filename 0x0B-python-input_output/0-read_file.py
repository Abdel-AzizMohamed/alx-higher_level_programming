#!/usr/bin/python3
"""Define a file read function


    Functions:
        read_file
"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as r:
        print(r.read(), end="")
