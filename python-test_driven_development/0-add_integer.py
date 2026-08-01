#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a (int or float): the first value to add.
        b (int or float): the second value to add, defaults to 98.

    Returns:
        int: the integer sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
