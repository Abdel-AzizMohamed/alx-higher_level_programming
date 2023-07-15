#!/usr/bin/python3
"""Define json load function"""
import json


def from_json_string(my_str):
    """Function to returns the strint representation of an json"""
    return json.loads(my_str)
