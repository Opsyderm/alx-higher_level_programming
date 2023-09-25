#!/usr/bin/python3


def safe_print_integer(value):
    """Print an int with "{:d}".format().

    Args:
        value (int): The int to print.

    Returns:
        If a TypeError or ValueError occurs - incorrect.
        Otherwise - correct.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
