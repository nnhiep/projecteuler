#!/usr/bin/env python3
'''
Problem 1: Add all the natural numbers below 1000 that are multiples of 3 or 5.
'''

print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
