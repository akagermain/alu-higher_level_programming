#!/usr/bin/python3
"""This module provides a function to list an object's available attributes and methods."""


def lookup(obj):
    """Return a list containing the attributes and methods available in an object."""
    return dir(obj)
