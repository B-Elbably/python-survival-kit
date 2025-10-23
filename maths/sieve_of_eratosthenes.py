def sieve_of_eratosthenes(max_n):  # O(n log log n)
    """Precompute prime status for numbers up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime


sieve = sieve_of_eratosthenes(10**5)
# build O(n log log n)
# query is_prime status in O(1) by index


"""
    Important -> Search about how to calculate T.C of Sieve of Eratosthenes
"""
