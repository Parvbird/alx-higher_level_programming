#!/usr/bin/python3


"""this defines save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """
    this serializes the python object and saves it to the file

    Args:
        my_obj: the python object
        filename: the file which the JSON string repre is to be written
    """
    with open(filename, 'w', encoding="UTF-8") as j_file:
        json.dump(my_obj, j_file)
