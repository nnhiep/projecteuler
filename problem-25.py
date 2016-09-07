#!/usr/bin/env python3
'''
What is the first term in the Fibonacci sequence to contain 1000 digits
'''


def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

n = 0
while True:
    x = fib(n)
    if len(str(x)) == 1000:
        print(n)
        break
    n += 1
