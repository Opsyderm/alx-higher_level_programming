#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of UTF8 text file.

    Args:
        filename (str): this is the name of the file to append to.
        text (str): this is the string to append to the file.
    Returns:
        return the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
