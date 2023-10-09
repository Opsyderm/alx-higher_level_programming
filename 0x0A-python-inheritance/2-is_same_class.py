#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of given class.

    Args:
        obj (any): This is the object to check.
        a_class (type): This is the class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class return true.
        Otherwise return false.
    """
    if type(obj) == a_class:
        return True
    return False
