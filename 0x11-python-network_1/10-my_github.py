#!/usr/bin/python3
"""display your github id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
