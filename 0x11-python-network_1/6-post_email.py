#!/usr/bin/python3
"""sends a POST request by using requests lib"""
import requests
import sys


if __name__ == "__main__":
    post = {"email": argv[2]}
    req = requests.post(sys.argv[1], data=post)

    print(req.text)
