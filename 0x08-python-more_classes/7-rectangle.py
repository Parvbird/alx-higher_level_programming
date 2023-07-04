#!/usr/bin/python3


"""This defines a Rectangle class."""


class Rectangle:
    """This represent a rectangle.

    Attributes:
        the number_of_instances (integer): The number of Rectangle instances.
        the print_symbol: The symbol used for string representation.
    """

    the number_of_instances = 0
    the print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes a new Rectangle.

        Args:
            width (integer): width of the new rectangle.
            height (integer): height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """This set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the width must be an integer")
        if value < 0:
            raise ValueError("the width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the height must be an integer")
        if value < 0:
            raise ValueError("the height must be >= 0")
        self.__height = value

    def area(self):
        """This return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """This return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """This return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """This print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
