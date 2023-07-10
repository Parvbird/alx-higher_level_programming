#!/usr/bin/python3


"""4-inherits_from module file"""


def inherits_from(obj, a_class):
    """
    this checks if object is an instance of a class that inherited
    {indirectly or directly} from the specified class

    Args:
        obj: the object ot be checked
        a_class: the type of class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
