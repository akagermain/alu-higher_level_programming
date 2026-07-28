#!/usr/bin/python3
"""This module provides a function for loading objects from JSON files."""

import json


def load_from_json_file(filename):
    """Return the Python object represented by the JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
