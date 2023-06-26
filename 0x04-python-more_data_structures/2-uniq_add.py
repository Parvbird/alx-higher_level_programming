#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list

    Args:
        my_list: a list of integer

    Return sum of unique integer
    """
    sum = 0
    new_list = list(set(my_list))
    for i in range(len(new_list)):
        sum += new_list[i]
    return sum
