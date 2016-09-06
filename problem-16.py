#!/usr/bin/env python3
'''
What is the sum of the digits of the number 21000?
'''


def pow2sum(n):
    pow = list(str(2 ** n))
    return sum(int(i) for i in pow)

print(pow2sum(1000))
