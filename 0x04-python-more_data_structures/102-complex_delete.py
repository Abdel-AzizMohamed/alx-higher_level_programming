#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = []
    for key, item in a_dictionary.items():
        if value == item:
            keys_list.append(key)
    for item in keys_list:
        del a_dictionary[item]
    new_dict = a_dictionary.copy()
    return new_dict
