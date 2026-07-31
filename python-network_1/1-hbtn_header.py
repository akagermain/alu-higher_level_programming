#!/usr/bin/python3
"""Takes in a URL, sends a request, and displays X-Request-Id header."""
import sys
from urllib import request
with request.urlopen(sys.argv[1]) as response:
    print(response.getheader("X-Request-Id"))
