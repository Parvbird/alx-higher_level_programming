#!/usr/bin/python3


"""this defines load_from_json_file() function"""
import json


def load_from_json_file(filename):
    """
    this deserializes the JSON string

    Args:
        filename: the filename or path to JSON file

    Return:
        the python object
    """
    with open(filename, encoding="UTF-8") as f:
        data = json.load(f)
        return data
