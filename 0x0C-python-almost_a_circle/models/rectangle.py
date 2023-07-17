#!/usr/bin/python3


""" this defines Rectangle class """
from models.base import Base


class Rectangle(Base):
    """the Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        this instantiates Rectangle instances

        Args:
            width: (integer) the width of Rectangle object
            height: (integer) the height of Rectangle object
            x: (int)
            y: (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ this returns string representation of Rectangle instance """
        str_rep = "[{}] ({}) {}/{} - {}/{}"
        idd, xx, yy, w = self.id, self.__x, self.__y, self.__width
        h = self.__height
        return str_rep.format(__class__.__name__, idd, xx, yy, w, h)

    @property
    def width(self):
        """this gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        this sets width

        Args:
            value: (integer) the value of width
        """
        if not isinstance(value, int):
            raise TypeError("the width must be an integer")
        if value <= 0:
            raise ValueError("the width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ this gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this sets height

        Args:
            value: (integer) the value of height
        """
        if not isinstance(value, int):
            raise TypeError("the height must be an integer")
        if value <= 0:
            raise ValueError("the height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ this gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """
        this sets x

        Args:
            value: (integer) the value of x
        """
        if not isinstance(value, int):
            raise TypeError("the value of x must be an integer")
        if value < 0:
            raise ValueError("the value of x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ this gets y """
        return self.__y

    @y.setter
    def y(self, value):
        """
        this sets y

        Args:
            value: (integer) the value of y
        """
        if not isinstance(value, int):
            raise TypeError("the value of y must be an integer")
        if value < 0:
            raise ValueError("the value of y must be >= 0")
        self.__y = value

    def area(self):
        """ this computes & returns the area of a Rectangle object """
        return (self.__width * self.__height)

    def display(self):
        """ this prints Rectangle instance with character '#' """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end="")
            for _ in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        this updates object attributes

        Args:
            args: the arguments for values of class attributes
            kwargs: the dictionary containing attributes and their values
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this returns the dictionary representation of a Rectangle object"""
        data = {}
        # this iterate over all attributes of the object
        for attr in self.__dict__:
            # this is to remove class name and '_' prefix of attribute name
            key = attr.lstrip('_').split('_')[-1]
            # this get the value of the attribute
            value = getattr(self, attr)
            # this collect data for serializable attributes
            data[key] = value
        return data
