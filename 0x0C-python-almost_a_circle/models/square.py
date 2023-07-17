#!/usr/bin/python3


""" this defines the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        this instantiates Square instances

        Args:
            size: (integer) the size of Square object
            x: (integer)
            y: (integer)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        this returns the string representation of Rectangle instance

        Note the width and height are equal for the Square object
        """
        str_rep = "[{}] ({}) {}/{} - {}"
        idd, xx, yy, w = self.id, self.x, self.y, self.width
        return str_rep.format(__class__.__name__, idd, xx, yy, w)

    @property
    def size(self):
        """ this returns object width """
        return self.width

    @size.setter
    def size(self, value):
        """
        the sets object's width

        Args:
            value: (integer) the value of object's width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        this updates object attributes

        Args:
            args: the arguments for values of class attributes
        """
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ this returns the dictionary representation of a Rectangle object"""
        data = {}
        # iterate over all attributes of the object
        for attr in self.__dict__:
            # this is to remove class name and '_' prefix of attribute name
            key = attr.lstrip('_').split('_')[-1]

            # this use 'size' instead of 'width' or 'height'
            if key == 'width' or key == 'height':
                key = 'size'

            # this get the value of the attribute
            value = getattr(self, attr)
            # this collecst data for serializable attributes
            data[key] = value
        return data
