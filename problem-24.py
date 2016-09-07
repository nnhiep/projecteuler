#!/usr/bin/env python3
'''
Find the millionth lexicographic permutation of the digits 0-9
'''
import itertools


x = itertools.permutations('0123456789', 10)
counter = 0
for i in x:
    counter += 1
    if counter == 1000000:
        print(''.join(i))
    else:
        pass
