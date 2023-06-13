#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    i = 0
    while i + 1 < len(my_list):
        if my_list[i + 1] >= max:
            max = my_list[i + 1]
        i += 1
    return max
