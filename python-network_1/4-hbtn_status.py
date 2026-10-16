#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status and displays response info."""
import requests


if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
    print("\t- utf8 content: {}".format(r.text))
