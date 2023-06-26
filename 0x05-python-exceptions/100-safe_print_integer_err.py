#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    prints the integer

    Args:
        value: value of the integer to print

    Return:
        True if the integer is printed, otherwise return False
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
