#!/usr/bin/python3
# 0-add_integer.py


"""this defines an integer addition function."""


def add_integer(a, b=98):
    """this returns the integer addition of a and b.

    Float arguments typecast to integer before addition is performed.

    Raises:
        TypeError: If either of a or b is a not integer and not float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("the a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("the b must be an integer")
    return (int(a) + int(b))
