#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    for item in a_dictionary.keys():
        if key == item:
            del a_dictionary[key]
            del new_dict[key]
            break
    return new_dict
