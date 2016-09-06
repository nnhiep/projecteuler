#!/usr/bin/env python3
'''
How many such routes are there through a 20×20 grid?

You will need to move N steps down, and N steps to the right.
That makes for N*2 total steps.

A path is simply an arrangement of these steps.
The number of ways to arrange the N*2 steps is (N*2)!.

But, since there are two sets of N identical steps,
we need to remove all the duplicate paths.

Thus, we divide by N! for each group, or by (N!)(N!).

So, the number of unique paths for an NxN grid is (2N)!(2N!)/(N!)(N!)
'''


def factorial(n):
        if n == 0:
            return 1
        else:
            return factorial(n-1) * n

print(int(factorial(40)/(factorial(20)*factorial(20))))
