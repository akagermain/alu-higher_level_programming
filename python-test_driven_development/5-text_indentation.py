#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """Print a text, with 2 new lines after each ., ? and :.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    length = len(text)
    i = 0
    while i < length:
        print(text[i], end="")
        if text[i] in {'.', '?', ':'}:
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
