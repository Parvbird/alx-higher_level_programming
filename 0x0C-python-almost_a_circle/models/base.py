#!/usr/bin/python3


"""Function that defines the Base class"""
import os
import json


class Base:
    """The Base class"""
    __nd_objects = 0

    def __init__(self, id=None):
        """
        this makes an instance if Base class

        Args:
            id: the id of Base class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this returns the JSON representation

        Args:
            list_dictionaries: the list of dictionaries

        Return:
            the JSON representation of @list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        json_rep = json.dumps(list_dictionaries, ensure_ascii=False)
        return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this save JSON representation of an object to a JSON file.

        First, it converts list of object(@list_objs) to
        list of the dictionary representation of objects.
        it saves the result to a json file of this format:
        <Class name>.json

        Args:
            list_objs: the list of objects
        """
        dict_list = []
        if list_objs:
            # this convert to list of dictionaries
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            # this get JSON representation of @dict_list
            json_rep = cls.to_json_string(dict_list)
            # this write to json file
            with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as file:
                file.write(json_rep)
        else:
            with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as file:
                json.dump(dict_list, file)

    def to_dictionary(self):
        """ this returns the dictionary representation of an object"""
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

    @staticmethod
    def from_json_string(json_string):
        """
        this deserializes the JSON string @json_string

        Args:
            json_string: the JSON string representation

        Return:
            the list of the JSON string representation @json_string
        """
        empty_list = []
        if not json_string:
            return empty_list
        else:
            json_rep = json.loads(json_string)
            return json_rep

    @classmethod
    def create(cls, **dictionary):
        """
        this returns an instance with all attributes already set

        Args:
            dictionary: this contains attributes and their data

        Return:
            the instance with all attributes already set
        """
        dummy_instance = cls(7, 2, 3)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        this loads data from a .json file & returns a list of instances

        Return:
            the list of instances
        """
        list_of_instances = []

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return list_of_instances
        else:
            # this open file and load json data
            with open(filename, "r", encoding="UTF-8") as file:
                json_data = json.load(file)

            # this convert data to json string
            json_string = json.dumps(json_data)

            # this convert to list of deserialized json string
            list_of_json_rep = cls.from_json_string(json_string)
            for attr in list_of_json_rep:
                list_of_instances.append(cls.create(**attr))
            return list_of_instances

    def update(self, *args, **kwargs):
        """
        this Updates object attributes

        Args:
            args: the arguments for values of class attributes
            kwargs: dictionary containing attributes and their values
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        this Save JSON representation of an object to a .csv file.

        First, it converts the list of object(@list_objs) to a
        list of the dictionary representation of objects.
        it saves the result to a .csv file of this format:
        <Class name>.csv

        Args:
            list_objs: a list of objects
        """
        dict_list = []
        if list_objs:
            # this convert to list of dictionaries
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            # this get JSON representation of @dict_list
            json_rep = cls.to_json_string(dict_list)
            # this write to .csv file
            with open(f"{cls.__name__}.csv", "w", encoding="UTF-8") as file:
                file.write(json_rep)
        else:
            with open(f"{cls.__name__}.csv", "w", encoding="UTF-8") as file:
                json.dump(dict_list, file)

    @classmethod
    def load_from_file_csv(cls):
        """
        this loads data from a .csv file & returns a list of instances

        Return:
            the list of instances
        """
        list_of_instances = []

        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return list_of_instances
        else:
            # this open file and load json data
            with open(filename, "r", encoding="UTF-8") as file:
                json_data = json.load(file)

            # this convert data to json string
            json_string = json.dumps(json_data)

            # this convert to list of deserialized json string
            list_of_json_rep = cls.from_json_string(json_string)
            for attr in list_of_json_rep:
                list_of_instances.append(cls.create(**attr))
            return list_of_instances
