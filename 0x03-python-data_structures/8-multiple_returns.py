#!/usr/bin/python3


def multiple_returns(sentence):
    """
    computes the length of a string and first character

    Args:
        sentence: (string)

    Return:
        a tuple with length of a string and its first character
    """
    str_len = len(sentence)
    if str_len == 0:
        first_chr = None
    else:
        first_chr = sentence[0]
    new_tuple = (str_len, first_chr)
    return new_tuple
