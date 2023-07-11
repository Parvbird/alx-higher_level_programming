#!/usr/bin/python3


"""this defines from_json_string() function"""
import json


def from_json_string(my_str):
    """
    this deserializes the json string to a python object

    Args:
        my_str: the variable holding json string

    Return:
        python object
    """
    p_obj = json.loads(my_str)
    return p_obj
