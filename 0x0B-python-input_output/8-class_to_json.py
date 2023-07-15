#!/usr/bin/python3
"""Defines a Python class to hson function."""


def class_to_json(obj):
    """Return the dictionary represntation of a given object"""
    return obj.__dict__
