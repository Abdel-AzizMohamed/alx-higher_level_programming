#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = []
    for key in a_dictionary.keys():
        sorted_list.append(key)
    sorted_list.sort()

    for item in sorted_list:
        print("{}: {}".format(item, a_dictionary[item]))
