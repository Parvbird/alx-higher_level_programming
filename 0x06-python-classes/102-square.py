#!/usr/bin/python3


"""the square module"""


class Square():
    """the square class"""

    def __init__(self, size=0):
        """
        this initializes the attributes of a Square instance

        Args:
            size: (integer) value of size attribute
        """
        self.__size = size

    @property
    def size(self):
        """this get the size of the square.

        Returns:
            int: The value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        this set the size of a Square object

        Args:
            size: (integer) of new value for the size attribute

        Raises:
            TypeError: if @size is not an integer
            ValueError: if @size is < 0
        """
        if isinstance(value, (int, float)):
            raise TypeError("the size must be a number")
        elif value < 0:
            raise ValueError("the size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """this computes and returns the area of a square object"""
        return self.__size ** 2

    def __eq__(self, other) -> bool:
        """this checks if object areas are ="""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """this checks if object areas are !="""
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        """this checks if one object area is > another"""
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """checks if one object area is >= to another"""
        return self.area() >= other.area()

    def __lt__(self, other) -> bool:
        """checks if one object area is < another"""
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """checks if one object area is <= to another"""
        return self.area() <= other.area()
