#!/usr/bin/python3
"""appends a string to a text file and returns # of characters"""


def append_write(filename="", text=""):
    """creating function"""
    with open(filename, 'w', encoding='utf-8' ) as f:
        return f.write(text)
