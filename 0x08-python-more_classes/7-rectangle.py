#!/usr/bin/python3

'''This module defines a class Rectangle'''


class Rectangle:
    '''
    This class defines a rectangle based on 0-rectangle.py

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        number_of_instances (int): number of instances of the rectangle
        print_symbol (any type): symbol used for string representation

    Methods:
        __init__: initializes a new rectangle
        width: getter method for width
        width.setter: setter method for width
        height: getter method for height
        height.setter: setter method for height
        area: returns the area of the rectangle
        perimeter: returns the perimeter of the rectangle
        __str__: returns the rectangle represented by the # character
        __repr__: returns a string representation of the rectangle
        __del__: deletes an instance of Rectangle
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        Initializes a rectangle instance with its attributes

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
        getter method for width

        Returns:
            The width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter method for width

        Args:
            value (int): width value to set to the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        getter method for height

        Returns:
            The height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        setter method for height

        Args:
            value (int): height value to set to the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        This method returns the area of the rectangle

        Returns:
            The area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        This method returns the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''
        This method returns the rectangle represented by the # character

        Returns:
            The rectangle represented by the # character
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        '''
        This method returns a string representation of the rectangle

        Returns:
            A string representation of the rectangle
        '''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''
        This method deletes an instance of Rectangle
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
