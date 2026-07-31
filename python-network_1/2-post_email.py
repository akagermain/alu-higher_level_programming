#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response body."""
from urllib import parse, request
import sys
data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")
with request.urlopen(sys.argv[1], data) as response:
    print(response.read().decode("utf-8"))
