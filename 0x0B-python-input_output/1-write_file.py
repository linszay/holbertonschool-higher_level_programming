#!/usr/bin/python3
"""writes a string to a text file and returns # of characters"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8' ) as f:
        return len(f.write(text))
