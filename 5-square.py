#!/usr/bin/python3


"""the square module"""


class Square():
    """the square class"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """this gets the size of the square.

        Returns:
            int: The int value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        this set the size of a square object

        Args:
            size: the (integer) new value for the size attribute

        Raises:
            TypeError: if @size is not an integer
            ValueError: if @size is < 0
        """
        if type(size) != int:
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this computes and returns the area of a square object"""
        return self.__size ** 2

    def my_print(self):
        """
        this prints a square using the '#' character
        """
        if self.__size <= 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
