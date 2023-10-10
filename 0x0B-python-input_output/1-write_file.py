#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to UTF8 text file.

    Args:
        filename (str): This is the name of the file to write.
        text (str): Thia is the text to write to the file.
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
