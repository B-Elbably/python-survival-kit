def build_prefix(arr): # O(n)
    n = len(arr)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + arr[i - 1]
    return pref

def range_sum(l, r): # O(1)
    return pref[r + 1] - pref[l]

arr = [1, 2, 3, 5, 4, 11, 1]
pref = build_prefix(arr)
print(range_sum(1, 3))  # Output: 10 (2 + 3 + 5)
