#!/usr/bin/python3
def uppercase(str):
    for char in str:
        letter = char
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            letter = chr(ord(char) - 32)
        print("{:s}".format(letter), end="")
    print("")
