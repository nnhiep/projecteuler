#!/usr/bin/env python3
'''
Problem 2: Find the sum of all the even-valued terms in the Fibonacci sequence
which do not exceed four million.
'''


# return a generator object (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..)
def fib():
    x, y = 1, 2
    while True:
        yield x
        x, y = y, x+y


def is_even(seq):
    for number in seq:
        if not number % 2:
            yield number


def under_four_million(seq):
    for number in seq:
        if number > 4000000:
            break
        yield number


print(sum(is_even(under_four_million(fib()))))
