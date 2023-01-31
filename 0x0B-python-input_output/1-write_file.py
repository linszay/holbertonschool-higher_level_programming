#!/usr/bin/python3
"""writes a string to a text file and returns # of characters"""


def write_file(filename="", text=""):
    """creating function"""
    with open(filename, 'w', encoding='utf-8' ) as f:
        return f.write(text)
