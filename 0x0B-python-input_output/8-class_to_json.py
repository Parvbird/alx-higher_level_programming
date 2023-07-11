#!/usr/bin/python3


"""this defines save_to_json_file() function"""


def class_to_json(obj):
    """this returns the dictionary description with the data structure"""
    data = {}

    # this would iterate over all attributes of the object
    for attr in obj.__dict__:
        # this get the value of the attribute
        value = getattr(obj, attr)
        # this collect data for serializable attributes
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
