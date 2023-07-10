#!/usr/bin/python3


"""1-my_list module file"""


class MyList(list):
    """the MyList class"""
    def print_sorted(self):
        """this sorts a list of integers in the ascending order"""
        if not all(isinstance(i, int) for i in self):
            raise TypeError("this must be a list of integers")
        print(sorted(self))
