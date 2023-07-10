#!/usr/bin/python3


"""3-is_kind_of_class module file"""


def is_kind_of_class(obj, a_class):
    """
    this checks if object is an instance of / or if object is an instance
    of a class that inherited from the specified class

    Args:
        obj: the object ot be checked
        a_class: the type of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
