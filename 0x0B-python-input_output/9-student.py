#!/usr/bin/python3


"""this defines a Student class"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """
        this makes and instance of the student instance

        Args:
            first_name: (str) first name
            last_name: (str) last name
            age: (int) age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this returns the dictionary description with the data structure"""
        data = {}

        # this iterate over all attributes of the object
        for attr in self.__dict__:
            # this would get the value of the attribute
            value = getattr(self, attr)
            # this collect data for serializable attributes
            if isinstance(value, (list, dict, str, int, bool)):
                data[attr] = value
        return data
