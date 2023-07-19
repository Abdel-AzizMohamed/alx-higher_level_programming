#!/usr/bin/python3
"""Define a base class"""
import json


class Base():
    """Define a base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init a new object"""
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if not list_dictionaries:
            return "[]"

        new_list = []
        for item in list_dictionaries:
            if not isinstance(item, dict):
                new_list.append(item.to_dictionary())
            else:
                new_list.append(item)

        return json.dumps(new_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""
        with open("{}.json".format(cls.__name__), "w") as w:
            data = cls.to_json_string(list_objs)
            w.write(data)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new_obj = cls(1, 1, 0, 0)
        for key, value in dictionary.items():
            new_obj.update(key=value)
        return new_obj
