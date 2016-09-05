#!/usr/bin/env python3
'''
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''


def square_of_sum(n):
    sum = ((n+1)*n)/2
    squared = sum**2
    return squared


def sum_of_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum


def difference(n):
    return int(square_of_sum(n) - sum_of_squares(n))

print(difference(100))
