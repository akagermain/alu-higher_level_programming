#!/usr/bin/python3
"""This module provides a function for converting objects to dictionaries."""


def class_to_json(obj):
    """Return a dictionary containing an object's serializable attributes."""
    return obj.__dict__
