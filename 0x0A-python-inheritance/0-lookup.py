#!/usr/bin/python3


"""0-lookup module file"""


def lookup(obj):
    """"
    this looks up the available attributes and methods of the object

    Args:
        obj: the object to look up

    Return:
        the list of available attributes and methods of the object
    """
    return dir(obj)
