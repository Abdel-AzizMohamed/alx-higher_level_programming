#!/usr/bin/python3
"""Define json dump function"""
import json


def to_json_string(my_obj):
    """Function to returns the JSON representation of an object"""
    return json.dumps(my_obj)
