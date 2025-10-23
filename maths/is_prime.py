"""
prime numbers 2,3,5,7,11,13,...
"""


def is_prime_1(n):  # O(√n)
    """Check if n is a prime number using trial division."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_2(n):  # O(√n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


"""
    what about O(1) query ??
    Check sieve of Eratosthenes in math/sieve_of_eratosthenes.py
"""
