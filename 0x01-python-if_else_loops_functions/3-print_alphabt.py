#!/usr/bin/python3
for numbers in range(97, 123):
    if (chr(numbers) != 'e' and chr(numbers) != 'q'):
        print('{}'.format(chr(numbers)), end='')
