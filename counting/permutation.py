from counting.binomial_coefficients import fac, inv


def perm(n, r):  # O(1)
    """:return: nPr mod p"""
    return fac[n] * inv[n - r]
