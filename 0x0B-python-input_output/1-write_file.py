#!/usr/bin/python3


"""This defines the write_file() method"""


def write_file(filename="", text=""):
    """
    it writes a string to a text file

    Args:
        filename: the name of file
        text: the string to be written

    Return:
        the number of characters that was written
    """
    with open(filename, 'w', encoding="UTF-8") as a_file:
        n_char = a_file.write(text)
    return n_char
