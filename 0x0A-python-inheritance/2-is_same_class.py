#!/usr/bin/python3
"""check if the obj is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """return using type to check"""
    return type(obj) is a_class
