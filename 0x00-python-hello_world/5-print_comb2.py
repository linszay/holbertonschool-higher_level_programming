#!/usr/bin/python3
numbers = range(0, 100)
for i in numbers:
    if (i < 10):
        print('0{}, '.format(i))
    elif (i >= 10 & i < 99):
        print('{}, '.format(i))
    else:
        print('99, \n')
