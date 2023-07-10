#!/usr/bin/python3


"""2-is_same_class module file"""


def is_same_class(obj, a_class):
    """
    this checks if object is the same instance of the specified class

    Args:
        obj: the object to be checked
        a_class: the type of class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
