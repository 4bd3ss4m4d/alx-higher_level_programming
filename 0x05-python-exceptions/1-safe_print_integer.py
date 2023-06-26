#!/usr/bin/python3

def safe_print_integer(value):
    '''Prints an integer with "{:d}".format().

    Args:
        value (int): The integer to print.
    Returns:
        True if value has been correctly printed (it means the value is an
        integer). False otherwise'''
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
