#!/usr/bin/python3
"""new class inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size
