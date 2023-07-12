#!/usr/bin/python3
"""class Student that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Initialize a new Students. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
