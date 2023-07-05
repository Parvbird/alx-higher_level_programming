#!/usr/bin/python3


"""This defines a locked class."""


class LockedClass:
    """
    This prevent the user from instantiating the new LockedClass attribute
    bc anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
