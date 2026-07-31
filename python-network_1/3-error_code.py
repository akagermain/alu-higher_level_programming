#!/usr/bin/python3
"""Sends a request to a URL and displays the response or the HTTP error code."""
from urllib import error, request
import sys
try:
    with request.urlopen(sys.argv[1]) as response:
        print(response.read().decode("utf-8"))
except error.HTTPError as err:
    print("Error code: {}".format(err.code))
