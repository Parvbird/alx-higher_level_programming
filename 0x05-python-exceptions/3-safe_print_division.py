#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides two integers and prints out result

    Args:
        a: the first integer
        b: the second integer

    Return:
        the result of dividing a / b or nothing if invalid
    """
    try:
        result = a / b
    except (ValueError, ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
