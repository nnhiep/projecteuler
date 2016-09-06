#!/usr/bin/env python3
'''
Find the sum of all the primes below 2.000.000.
'''


def sum_primes(limit):
    primes = []
    for n in range(2, limit+1):
        for p in primes:
            if n % p == 0:
                break             # if p divides n, stop the search
            if n < p*p:
                primes.append(n)  # if p > sqrt(n), mark n as prime and stop
                break
        else:
            primes.append(n)  # fallback: only get here for n == 2

    return sum(int(i) for i in primes)

print(sum_primes(2000000))
