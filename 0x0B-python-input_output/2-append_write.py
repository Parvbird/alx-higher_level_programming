#!/usr/bin/python3


"""this defines the append_write() method"""


def append_write(filename="", text=""):
    """
    This appends the string to the end of a text file

    Args:
        filename: the name of file
        text: the string to be appended

    Return:
        the number of characters that was appended
    """
    with open(filename, 'a', encoding="UTF-8") as a_file:
        n_char = a_file.write(text)
    return n_char
