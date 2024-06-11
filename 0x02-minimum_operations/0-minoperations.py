#!/usr/bin/python3
"""
Module to calculates the minimum amount of operations
needed to print 'H' n times.
"""
from typing import List


def factors_gen(n: int) -> List[int]:
    """
    time = O(n^2)
    Returns:
        The list of all prime factors of n
    """
    factor_list = []

    i = 1
    while i <= n:
        if n % i == 0 and i != 1:
            prime = True
            # check if i is a prime number
            for j in range(1, i + 1):
                if i % j == 0 and j != 1 and i != j:
                    prime = False
                    break

            if prime is True:
                factor_list.append(i)
                n //= i
                i = 1

        i += 1
    return factor_list


def minOperations(n: int) -> int:
    """
    calculates the minimum amount of operations
    needed to print 'H' n times.
    Returns:
        The amount of operations
        or
        0, if achieving n is impossible
    """
    if n <= 1:
        return 0

    factors = factors_gen(n)
    operations = 0

    for factor in factors:
        operations += factor

    return operations
