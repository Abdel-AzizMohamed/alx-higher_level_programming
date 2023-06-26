#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    roman_dict = {"I": 1, "v": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    for roman in roman_string:
