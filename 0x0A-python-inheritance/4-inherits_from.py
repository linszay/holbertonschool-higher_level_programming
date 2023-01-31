#!/usr/bin/python3
"""checks if obj is instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """checks if obj is instance inherited or not"""
    return isinstance(obj, a_class) and type(obj) is not a_class
