#!/usr/bin/python3

'''Define a class Square'''


class Square:
    '''
    A class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Initialize a new square.
        area: Calculate the area of the square.
        size: Getter function for size attribute.
        size.setter: Setter function for size attribute.
    '''
    def __init__(self, size=0):
        '''
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Getter function for size attribute.

        Returns:
            The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter function for size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            The area of the square.
        '''
        return self.__size ** 2
