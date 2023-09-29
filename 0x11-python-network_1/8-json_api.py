#!/usr/bin/python3
"""takes in a letter and sends a POST with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        payload = {"q": ""}
    else:
        payload = {"q": sys.argv[1]}
    req = requests.post(url, data=paylaod)

    print(req.text)
