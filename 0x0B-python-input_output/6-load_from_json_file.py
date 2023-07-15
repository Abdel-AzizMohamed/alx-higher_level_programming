#!/usr/bin/python3
"""Define json save function"""
import json


def load_from_json_file(filename):
    """Function to returns the strint representation of an json"""
    with open(filename, "r", encoding="UTF-8") as r:
        readed_data = json.load(r)
    return readed_data
