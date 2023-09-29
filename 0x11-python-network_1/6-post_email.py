#!/usr/bin/python3
"""sends a POST request by using requests lib"""
import requests
import sys


if __name__ == "__main__":
    post = {"email": argv[2]}
    req = requests.get(sys.argv[1], params=post)

    print(req.text)
