# mod is 1e9+7 by default
"""
Regular power or (**) in python is O(n). not O(1) or O(log n)
fast power (binary exponentiation) is O(log n)
"""


def fast_power(base, exp, mod=10**9 + 7):  # O(log n)
    """Compute (base^exp) % mod using binary exponentiation."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # odd -> multiply base with result
            result = (result * base) % mod
        exp = exp >> 1  # == exp // 2
        base = (base * base) % mod
    return result


def fast_pow_recursive(base, exp, mod=10**9 + 7):  # O(log n)
    """Compute (base^exp) % mod using recursive binary exponentiation."""
    if exp == 0:
        return 1 % mod
    half = fast_pow_recursive(base, exp // 2, mod)
    half = (half * half) % mod
    if exp % 2 == 1:  # odd exponent
        half = (half * base) % mod
    return half
