#!/usr/bin/python3


"""This adds arguments to a python list"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# this create an empty list
my_list = []

# this get the arguments from command line
arguments = sys.argv[1:]

# this checks if json file exists
# and if valid the a python object is then returned
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

# this append new argumnts
my_list.extend(arguments)

# the final serialized python object
save_to_json_file(my_list, "add_item.json")
