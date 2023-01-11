#!/usr/bin/python3
def safe_print_divisions(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: '.format(result))
        return result
