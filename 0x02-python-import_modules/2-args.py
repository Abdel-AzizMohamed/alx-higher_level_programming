#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv

    if len(args) == 1:
        print("{:d} argument.".format(0))
    else:
        print("{:d} argument:".format(len(args) - 1))

    for i, item in enumerate(args):
        if i == 0:
            continue
        print("{:d}: {}".format(i, item))
