#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    replaces an element at an index position
    without modifying the original list

    Args:
        my_list: list of integers
        idx: position of element to replace
        element: new element

    Return:
        copy of list if idx is negative not in range
        else, the new list
    """
    dup_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return dup_list
    dup_list[idx] = element
    return dup_list
