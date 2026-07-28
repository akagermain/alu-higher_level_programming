#!/usr/bin/python3
"""This module provides a function for saving objects as JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object's JSON representation to the specified file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
