#!/usr/bin/python3


"""the square module"""


class Square():
    """the Square class"""
    def __init__(self, size=0):
        """to iniatializes an instance attribute"""
        if type(size) != int:
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size

    def area(self):
        """this computes and returns the area of a square object"""
        return self.__size ** 2
