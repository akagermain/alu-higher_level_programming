#!/usr/bin/python3
"""Module that prints a square using the character #."""


def print_square(size):
    """Print a square of the character # with the given size.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is an integer less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
