#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''Prints the first x elements of a list and only integers.

    Args:
        my_list (list): The list to print.
        x (int): The number of elements to print.
    Returns:
        The number of integers printed.'''
    ints_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            ints_printed += 1
    print("")
    return ints_printed
