#!/usr/bin/python3
numbers = range(0, 100)
for i in numbers:
    if (i < 99):
        print('{:02}'.format(i), end=', ')
    else:
        print('{}'.format(i))
