#!/usr/bin/python3

'''Define a class Square'''


class Square:
    '''
    A class to represent a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__: Initialize a new square.
        area: Calculate the area of the square.
        size: Getter function for size attribute.
        size.setter: Setter function for size attribute.
        position: Getter function for position attribute.
        position.setter: Setter function for position attribute.
        my_print: Print the square to stdout using the # character.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''
        Getter function for position attribute.

        Returns:
            The position of the square.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter function for position attribute.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        Returns:
            None
            '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
        Calculate the area of the square.

        Returns:
            The area of the square.
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Print the square to stdout using the # character.

        Returns:
            None'''
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
