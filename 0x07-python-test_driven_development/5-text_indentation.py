#!/usr/bin/python3

'''
This module contains a function that prints a text with 2 new lines after each
 of these characters: ., ? and :.
'''


def text_indentation(text):
    '''
    Function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text: text to print

    Raises:
        TypeError: If text is not a string.

    Returns:
        None.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char == '?' or char == '.' or char == ':':
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
