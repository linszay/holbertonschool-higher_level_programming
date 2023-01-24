#!/usr/bin/python3
"""Creating a class named Rectangle."""


class Rectangle:
    """Giving the class an instantiation."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif size < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif size < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
