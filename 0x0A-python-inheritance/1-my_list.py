#!/usr/bin/python3
"""write a new class that inherits from list"""


class MyList(list):
    """MyList inherites from list"""
    def print_sorted(self):
        print(sorted(self))
