#!/usr/bin/python3
"""Square Class"""


class Square:
    """Defines a class named Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, valx):
        if not isinstance(valx, int):
            raise TypeError("size must be an integer")
        elif valx < 0:
            raise ValueError("size must be >= 0")
        self.__size = valx

    def area(self):
        return self.__size ** 2
