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
        area: Calculate the area of the square.
    '''
    def __init__(self, size=0):
        '''
        Initialize Square with size attribute

        Args:
            size (int): Size of the square side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            The area of the square.
        '''
        return self.__size ** 2
