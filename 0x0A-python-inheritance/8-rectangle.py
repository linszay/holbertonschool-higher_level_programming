#!/usr/bin/python3
"""creating subclass Rectangle"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", int)
        self.integer_validator("height", int)
       