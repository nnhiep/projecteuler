#!/usr/bin/env python3


def fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def is_even(x):
    return x % 2 == 0


def problem2():
    sum_even_fibs = 0

    THRESHOLD = 4000000  # constant
    i = 1
    fibi = fib(i)

    while fibi < THRESHOLD:
        if is_even(fibi):
            sum_even_fibs += fibi
        i += 1
        fibi = fib(i)
    return sum_even_fibs

print(problem2())
