#!/usr/bin/python3
"""Define a file read function


    Functions:
        write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """write content to a file"""
    with open(filename, "w", encoding="UTF-8") as w:
        char_count = w.write(text)
    return char_count
