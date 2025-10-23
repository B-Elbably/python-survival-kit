"""
    Number of permutations where no element is in its original position:
    !n = n! × Σ(-1)ᵏ / k!  for k=0 to n
    ==> !n = round(n! / e)
    n! => factorial of n
    !n => derangement of n
    e => Euler's number
"""
MAXN = 10**6
d = [0] * (MAXN + 1)  # derangement array
# build O(n) 
# query O(1)
def prepare_derangements(p: int):
    """Precompute derangements up to MAXN using recurrence."""
    global d
    d[0] = 1
    d[1] = 0
    for i in range(2, MAXN + 1):
        d[i] = ((i - 1) * (d[i - 1] + d[i - 2])) % p

