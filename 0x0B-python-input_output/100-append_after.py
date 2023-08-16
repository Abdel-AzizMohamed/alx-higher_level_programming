#!/usr/bin/python3
"""Define A line repalce function"""


def append_after(filename="", search_string="", new_string=""):
    """insert a string line a fter if search_string found"""
    new_data = ""
    with open(filename, "r", encoding="UTF-8") as r:
        for line in r.readlines():
            new_data += line
            if line.find(search_string) != -1:
                new_data += new_string
    with open(filename, "w", encoding="UTF-8") as w:
        w.write(new_data)
