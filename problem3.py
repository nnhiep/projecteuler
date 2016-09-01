#!/usr/bin/env python3
'''
The prime factors of 13195 are 5, 7, 13 and 29.
Find the largest prime factor of 600851475143
'''


def prime(n):
    primefac = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            primefac.append(d)
            n = int(n/d)
        d += 1
    if n > 1:
        primefac.append(n)
    return primefac

plist = prime(600851475143)
print(plist[len(plist)-1])
