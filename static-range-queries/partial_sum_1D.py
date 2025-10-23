# partial sum is static range query
# Difference array approach
def build_partial(queries):  # O(n)
    n = len(arr)
    diff = [0] * (n + 1)
    for l, r, val in queries:
        diff[l] += val
        diff[r + 1] -= val
    # prefix sum to get final values
    for i in range(1, n + 1):
        diff[i] += diff[i - 1]
    return diff[::-1]


def build_prefix(arr):  # O(n)
    n = len(arr)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + arr[i - 1]
    return pref


def range_sum(l, r):  # O(1)
    # print(pref[r + 1] , pref[l])
    return pref[r + 1] - pref[l]


arr = [1, 2, 3, 4, 5]
# Example usage
queries = [
    # (l, r, value to add to all elements in range)
    # 0-based indexing
    (1, 3, 10),
    (0, 2, 5),
    (2, 4, 2),
    (0, 4, 1),
]

difference_array = build_partial(queries)
# array after all range updates
for i in range(len(arr)):
    arr[i] += difference_array[i]

pref = build_prefix(arr)
print(range_sum(1, 3))  # Output the sum in range [1, 3]
print(range_sum(0, 4))  # Output the sum in range [0, 4]

"""
    Search about shallow copy and deep copy
"""
