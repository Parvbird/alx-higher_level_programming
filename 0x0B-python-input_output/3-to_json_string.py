#!/usr/bin/python3


"""this defines to_json_string() function"""
import json


def to_json_string(my_obj):
    """
    this serializes an object

    Args:
        my_obj: the object to be serialized

    Return:
        the json representation of @my_obj
    """
    j_rep = json.dumps(my_obj)
    return j_rep
