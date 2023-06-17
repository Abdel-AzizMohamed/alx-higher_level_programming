#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = ""
    max_score = 0
    i = 0
    for key, item in a_dictionary.items():
        if i == 0:
            max_key = key
            max_score = item
        elif max_score < item:
            max_score = item
            max_key = key
        i += 1
    return max_key
