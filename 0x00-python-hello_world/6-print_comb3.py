#!/usr/bin/python3
first_number = range(0, 10)
second_number = range(0,10)
for i in first_number:
    for j in first_number:
        if (i!=j & j!=i):
            print('{}{}'.format(i, j), end=', ')
        else:
            print('{}'.format(i))