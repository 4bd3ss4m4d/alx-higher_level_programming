#!/usr/bin/python3

def magic_calculation(a, b):
    '''Performs the magic calculation
    Args:
        a (int): The first value.
        b (int): The second value.
    Returns:
        The result of the calculation.'''
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)
