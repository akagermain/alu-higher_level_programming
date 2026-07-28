#!/usr/bin/python3
"""This module provides a function for writing text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of characters
    written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
