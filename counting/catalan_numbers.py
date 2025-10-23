from counting.binomial_coefficients import comb, exp


def catalan(n, p):  # O(1)
    if n == 0:
        return 1
    return comb(2 * n, n, p) * exp(n + 1, p - 2, p) % p


MOD = 10**9 + 7
print(catalan(5, MOD))  # Output: 42
