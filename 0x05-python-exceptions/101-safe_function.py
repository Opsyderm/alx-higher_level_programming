#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes function safely.

    Args:
        fct: This is the function to execute.
        args: Arg for fct.

    Returns:
        If an error occurs return None.
        Otherwise return the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
