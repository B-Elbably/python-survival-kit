from combinatorics.binomial_coefficients import comb

# Queries O(1)


def stars_bars_nonnegative(n, k):
    """Number of non-negative solutions to x1 + ... + xk = n"""
    return comb(n + k - 1, k - 1)


def stars_bars_positive(n, k):
    """Number of positive solutions to x1 + ... + xk = n"""
    return comb(n - 1, k - 1)


def stars_bars_lower_bounds(n, k, lower_bounds):
    """Number of solutions to x1 + ... + xk = n with xi >= ai"""
    total_lower = sum(lower_bounds)
    if n < total_lower:
        return 0
    return comb(n - total_lower + k - 1, k - 1)
