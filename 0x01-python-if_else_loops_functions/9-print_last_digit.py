#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num = -number

    print("{:d}".format(num % 10), end="")
    return num % 10
