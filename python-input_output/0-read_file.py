#!/usr/bin/python3
"""This module provides a function for reading and printing a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to standard output."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
