#!/usr/bin/python3
"""This module provides a function for converting JSON strings to objects."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
