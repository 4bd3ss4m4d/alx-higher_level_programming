#!/usr/bin/python3

'''This module contains a function that adds 2 integers.'''


def add_integer(a, b=98):
    '''
    Function that adds 2 integers.

    Args:
        a: first integer
        b: second integer

    Returns:
        The addition of a and b.
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
