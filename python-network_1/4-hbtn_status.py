#!/usr/bin/python3
"""Fetches a URL using requests and displays information about the response body."""
import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
