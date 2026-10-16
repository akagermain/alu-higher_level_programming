#!/usr/bin/python3
"""Sends a request to a URL and prints the body or HTTP error code."""
from urllib import error, request
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
