#!/usr/bin/python3
def uppercase(C):
    for i in C:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(C) - 32)
        print('{}'.format(i), end='')
    print('')
