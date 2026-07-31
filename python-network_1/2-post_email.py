#!/usr/bin/python3
"""Sends a POST request to a URL with an email parameter and prints body."""
from urllib import parse, request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({"email": email}).encode("utf-8")
    with request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode("utf-8"))
