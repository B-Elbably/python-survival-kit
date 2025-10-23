# pow(a, phi(m) - 1, m)  # if gcd(a,m)=1
# When you see:"count numbers co-prime to n", "modular inverses", "primitive roots" → use φ(n)
"""
Search about Euler's Totient Function
Co-prime numbers
primitive roots
"""


def phi(n):  # O(sqrt(n))
    """Calculate Euler's Totient Function φ(n)"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


# build phi values up to MAXN
MAXN = 10**6
phi_values = [0] * (MAXN + 1)


def build_phi():
    """Precompute φ(i) for i = 1 to MAXN using a sieve approach."""
    global phi_values
    for i in range(1, MAXN + 1):
        phi_values[i] = i
    for i in range(2, MAXN + 1):
        if phi_values[i] == i:  # i is prime
            for j in range(i, MAXN + 1, i):
                phi_values[j] -= phi_values[j] // i


build_phi()
# query phi values in O(1) by index


def is_primitive_root(g, n, factors: list[int]):
    """
    Check if g is primitive root modulo n
    factors: prime factors of φ(n)
    """
    phi_n = phi(n)
    for p in factors:
        if pow(g, phi_n // p, n) == 1:
            return False
    return True
