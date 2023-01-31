#!/usr/bin/python3
"""returns dictionary description w/ simple data struct
    for JSON sterilization of obj"""


def class_to_json(obj):
    """creating function"""
    return obj.__dict__
