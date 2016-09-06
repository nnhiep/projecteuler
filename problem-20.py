#!/usr/bin/env python3
'''
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


def sum_digits(n):
    return sum(int(i) for i in str(factorial(n)))


print(sum_digits(100))
