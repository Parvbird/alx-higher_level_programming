#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    cout = 0
    for i in my_list:
        try:
            if cout == x:
                break
            print("{:d}".format(i), end="")
            cout += 1
        except Exception as e:
            pass
    print()
    return cout
