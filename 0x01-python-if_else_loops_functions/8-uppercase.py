#!/usr/bin/python3
def uppercase(C):
    for i in C:
        if ord(C) > 96 and ord(C) < 123:
            C = chr(ord(C) - 32)
        print('{}'.format(C), end='')
        print('')
