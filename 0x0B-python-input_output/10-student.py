#!/usr/bin/python3
"""adding new method"""


class Student:
    """creating new method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
