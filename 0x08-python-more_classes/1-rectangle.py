
#!/usr/bin/python3


"""This defines a Rectangle class."""


class Rectangle:
    """This represent a rectangle."""

    def __init__(self, width=0, height=0):
        """This initializes a new Rectangle.

        Args:
            width (int): The main width of the new rectangle.
            height (int): The main height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
