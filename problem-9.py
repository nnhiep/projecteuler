#!/usr/bin/env python3
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def prod_triplet(n):
    for i in range(1, n):
        for j in range(1, n-i):
            k = n-i-j
            if i**2 + j**2 == k**2:
                return i*j*k

print(prod_triplet(1000))
