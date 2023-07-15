#!/usr/bin/python3
"""Define a file append function


    Functions:
        append_file(filename="", text="")
"""


def append_write(filename="", text=""):
    """append content to a file"""
    with open(filename, "a", encoding="UTF-8") as a:
        char_count = a.write(text)
    return char_count
