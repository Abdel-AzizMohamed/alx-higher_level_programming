#!/usr/bin/python
"""Define a file read function


    Functions:
        write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as w:
        char_count = w.write(text)
    return char_count
