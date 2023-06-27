#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    it divides the element by element of two lists and store result in new list
    If an error, result at that index is equals zero

    Args:
        my_list_1: the first list
        my_list_2: the second list
        list_length: the length of new list

    Return:
        my new list
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
