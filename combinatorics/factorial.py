from combinatorics.binomial_coefficients import fac


def factorial(n):  # O(1)
    """:return: n! mod p"""
    return fac[n]


print(factorial(5))  # Output: 120
