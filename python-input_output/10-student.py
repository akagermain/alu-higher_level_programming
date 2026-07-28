#!/usr/bin/python3
"""This module defines a Student class with filtered JSON serialization."""


class Student:
    """Represent a student with a name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation with selected attributes."""
        if isinstance(attrs, list):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__
