#!/usr/bin/python3
"""displays the value of the variable X-Request-Id by requests lib"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])

    print(req.headers.get("X-Request-Id"))
