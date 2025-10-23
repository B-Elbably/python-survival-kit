"""
    # For 3 sets:
    |A ∪ B ∪ C| = |A| + |B| + |C|
                - |A ∩ B| - |A ∩ C| - |B ∩ C|
                + |A ∩ B ∩ C|
"""

"""
    General form:
    # |A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
"""

# try to solve:
# 1- https://codeforces.com/contest/2125/problem/C


# 2- https://cses.fi/problemset/task/2185 (important)
def inclusion_exclusion(n, a): # O(2^k * k)
    """
    a (list[int]): list of divisors

    Returns:
        int: count of integers ≤ n divisible by at least one element in a
    """
    k = len(a)
    ans = 0
    for i in range(1, 1 << k):  # iterate all non-empty subsets
        now = 1
        ss = 0
        for j in range(k):
            if (i >> j) & 1:
                now *= a[j]
                ss += 1
                if now > n:
                    break  # optimization: skip if product too big

        if now > n:
            continue
        ans -= ((-1) ** ss) * (n // now)
    return ans
