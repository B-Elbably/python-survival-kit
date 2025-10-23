def spf(n):  # O(n log log n)
    """Returns smallest prime factor for each number from 1 to n in O(n log log n) time and O(n) space."""
    spf = [0] * (n + 1)
    spf[1] = 1
    for i in range(2, n + 1):
        if spf[i] == 0:  # i is prime
            spf[i] = i
            for j in range(i * i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf
