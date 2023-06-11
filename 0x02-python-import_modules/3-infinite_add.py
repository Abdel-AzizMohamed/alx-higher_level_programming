#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0

    for i, item in enumerate(sys.argv):
        if i == 0:
            continue
        result += int(item)
    print(result)
