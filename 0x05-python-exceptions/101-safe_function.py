#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    '''Executes a function safely.
    Args:
        fct (function): The function to execute.
        args (list): The arguments of the function.
    Returns:
        The result of the function.'''
    try:
        return fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
