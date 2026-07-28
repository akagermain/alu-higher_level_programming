#!/usr/bin/python3
"""This module defines a class that extends the built-in list class."""


class MyList(list):
    """Represent a list with a method for printing sorted elements."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
