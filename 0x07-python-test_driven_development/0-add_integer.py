#!/usr/bin/python3
""" 0-add_integer"""


def add_integer(a, b=98):
    """adds two integers."""
    if not isinstance(float, a) or not isinstance(int, a):
        raise TypeError('a must be an integer')
    if not isinstance(float, b) or not isinstance(int, b):
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
