from factorial_and_comb import comb, exp

def catalan(n: int, p: int):
    if n == 0:
        return 1
    return comb(2 * n, n, p) * exp(n + 1, p - 2, p) % p

MOD = 10**9 + 7
print(catalan(5, MOD))  # Output: 42