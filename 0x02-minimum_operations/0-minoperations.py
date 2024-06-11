#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """
    a function that returns an integer that is the number of minimum operations
    """
    if n > 1:
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        numOperations = 0
        for n in factors:
            numOperations += n
        return numOperations
    else:
        return 0
