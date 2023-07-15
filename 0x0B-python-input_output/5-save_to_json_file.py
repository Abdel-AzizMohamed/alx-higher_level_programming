#!/usr/bin/python3
"""Define json save function"""
import json


def save_to_json_file(my_obj, filename):
    """Function to returns the strint representation of an json"""
    with open(filename, "w", encoding="UTF-8") as w:
        json.dump(my_obj, w)
