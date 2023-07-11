#!/usr/bin/python3


"""this defines the read_file() method"""


def read_file(filename=""):
    """
    it reads the text file and prints its content to stdout

    Args:
        filename: the name of text file
    """
    with open(filename, "r", encoding="UTF-8") as a_file:
        text = a_file.read()
        print(text, end="")
