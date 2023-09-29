#!/usr/bin/python3
"""sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    post_values = {"email": sys.argv[2]}
    post = urllib.parse.urlencode(post_values)
    post = post.encode("ascii")

    request = urllib.request.Request(url, post)
    with urllib.request.urlopen(request) as response:
        data = response.read()

    print(data.decode("utf-8"))
