#!/usr/bin/python3

'''
This module contains a function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
    Function that prints My name is <first name> <last name>.

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        Nothing.
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
