#!/usr/bin/python3


"""7-base_geometry module file"""


class BaseGeometry:
    """the  BaseGeometry class"""
    def area(self):
        """this is a public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this validates a value

        Args:
            name: the attribute name
            value: the attribute value

        Raise(s):
            TypeError: if @value is ! int
            ValueError: if @value is <= 0
        """
        if type(value) != int:
            raise TypeError(f"{name} this must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} this must be greater than 0")
