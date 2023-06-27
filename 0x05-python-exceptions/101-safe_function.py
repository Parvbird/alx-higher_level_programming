#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    executes the function in a safe way

    Args:
        fct: the function to be executed
        args: the arbitrary argument lists

    Return:
        the result of function executed, otherwise nothing
    """
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
