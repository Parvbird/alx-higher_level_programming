#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of the  list and only integer

    Args:
        my_list: (list) integer
        x: number of elements to access in  the@my_list

    Return:
        number of elements  to be printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
