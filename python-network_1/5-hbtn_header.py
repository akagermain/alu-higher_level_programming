#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id response header."""
import requests
import sys
response = requests.get(sys.argv[1])
print(response.headers.get("X-Request-Id"))
