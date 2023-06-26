#!/usr/bin/python3
def element_at(my_list, idx):
    """
    retrieves an element from a list

    Args:
        my_list: list of integers
        idx: index of element to retrieve

    Return:
        None if idx is negative or out of range
        else, the element at idx
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
