#!/usr/bin/python3
"""the square module"""


class Square():
    """the square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """this get the size of the square.

        Return:
            int: the value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        this set the size of a square object

        Args:
            size: (integer) new value for the size attribute

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

    @property
    def position(self):
        """
        this get position of the square object

        Return:
            the position of the square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        this set position of the square object

        Args:
            value: the (tuple) position of the square object

        Raises:
            TypeError: if @value is ! a tuple of integer
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("the position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("the position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """this computes and returns the area of the square object"""
        return self.__size ** 2

    def my_print(self):
        """
        this prints a square using the '#' character
        """
        if self.__size <= 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
