#!/usr/bin/python3
"""
Get the amount of minimum operations required to copy a character
a specific amount of time
"""


def primeFactors(n):
    """
    Use the sieve of Eratosthenes to get prime factors of a given number
    """
    spf = [0 for i in range(n+1)]
    spf[1] = 1
    for i in range(2, n+1):
        spf[i] = i
    for i in range(4, n+1, 2):
        spf[i] = 2

    for i in range(3, int(n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i

    lilac = []
    while n != 1:
        lilac.append(spf[n])
        n = n // spf[n]
    return (lilac)


def minOperations(n):
    """
    Get the minimum operations needed for the operations
    """
    try:
        prime_factors = primeFactors(n)
        final = sum(prime_factors)
        return (final)
    except Exception:
        return (0)
