#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """This will Print an int with "{:d}".format().

    If a ValueError message is seen, a corresponding
    message will be printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
