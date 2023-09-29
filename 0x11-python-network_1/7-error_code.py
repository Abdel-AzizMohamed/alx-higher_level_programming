#!/usr/bin/python3
"""displays the body of the response & handel http error"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
