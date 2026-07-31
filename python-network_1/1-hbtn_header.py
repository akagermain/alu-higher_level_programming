#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id response header."""
from urllib import request
import sys
with request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
