#!/usr/bin/python3
""" 0-add_integer"""


def add_integer(a, b=98):
    """adds two integers."""
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
