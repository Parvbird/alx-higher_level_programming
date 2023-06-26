#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    computes a set of all elements present in only one set

    Args:
        set_1: list one
        set_2: list two

    Return:
        a set of all elements present in only one set
    """
    return set_1.symmetric_difference(set_2)
