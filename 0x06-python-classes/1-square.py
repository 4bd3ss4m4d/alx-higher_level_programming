#!/usr/bin/python3

'''Define a class Square'''


class Square:
    '''
    A class representing a square shape.

    This class provides functionality to create and manipulate square objects.

    Attributes:
        __size (int): The size of the square side.

    Methods:
        __init__: Initialize the Square with a specified size.
    '''
    def __init__(self, size):
        '''
        Initialize Square with size attribute

        Args:
            size (int): Size of the square side.
        '''
        self.__size = size
