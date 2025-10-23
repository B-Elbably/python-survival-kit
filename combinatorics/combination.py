from binomial_coefficients import fac, inv


def comb(n, r, p):  # O(1)
    """:return: nCr mod p"""
    if fac[0] == 0:
        raise RuntimeError(
            "factorials not initialized — call prepare(p) before using comb"
        )
    return fac[n] * inv[r] % p * inv[n - r] % p
