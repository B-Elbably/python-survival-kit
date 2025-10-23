MAXN = 10**6

fac = [0] * (MAXN + 1)
inv = [0] * (MAXN + 1)

def exp(x: int, n: int, m: int) -> int:
    """:return: x^n modulo m in O(log p) time."""
    x %= m  # note: m * m must be less than 2^63 to avoid ll overflow
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % m
        x = (x * x) % m
        n //= 2
    return res


def factorial(p: int):
    """Precomputes n! from 0 to MAXN."""
    global fac
    fac[0] = 1
    for i in range(1, MAXN + 1):
        fac[i] = (fac[i - 1] * i) % p


def inverses(p: int):
    """
    Precomputes all modular inverse factorials from 0 to MAXN in O(n + log p) time
    """
    global inv
    inv[MAXN] = exp(fac[MAXN], p - 2, p)
    for i in range(MAXN, 0, -1):
        inv[i - 1] = (inv[i] * i) % p


def comb(n: int, r: int, p: int):
    """:return: nCr mod p"""
    if fac[0] == 0:
        raise RuntimeError("factorials not initialized — call prepare(p) before using comb")
    return fac[n] * inv[r] % p * inv[n - r] % p


def factorial_value(n: int) -> int:
    """:return: n! mod p"""
    return fac[n]


def perm(n: int, r: int) -> int:
    """:return: nPr mod p"""
    return fac[n] * inv[n - r]

def prepare(p: int):
    """Convenience: compute fac and inv tables for modulus p."""
    factorial(p)
    inverses(p)

prepare(10**9 + 7)