# 2D Difference Array

def build_partial_2d(n, m, queries):  # O(q)
    diff = [[0] * (m + 2) for _ in range(n + 2)]
    for x1, y1, x2, y2, val in queries:
        diff[x1][y1] += val
        diff[x1][y2 + 1] -= val
        diff[x2 + 1][y1] -= val
        diff[x2 + 1][y2 + 1] += val

    for i in range(n):
        for j in range(1, m):
            diff[i][j] += diff[i][j - 1]

    for j in range(m):
        for i in range(1, n):
            diff[i][j] += diff[i - 1][j]

    return [row[:m] for row in diff[:n]]


def build_prefix_2d(mat):  # O(n*m)
    n, m = len(mat), len(mat[0])
    pref = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = mat[i - 1][j - 1] \
                        + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1]

    return pref


def range_sum_2d(pref, x1, y1, x2, y2):  # O(1)
    # inclusive coordinates
    return (
        pref[x2 + 1][y2 + 1]
        - pref[x1][y2 + 1]
        - pref[x2 + 1][y1]
        + pref[x1][y1]
    )


# Example usage
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n, m = len(arr), len(arr[0])

queries = [
    (0, 0, 1, 1, 10),  # add +10 to submatrix (0,0)-(1,1)
    (1, 1, 2, 2, 5),   # add +5 to submatrix (1,1)-(2,2)
    (0, 1, 1, 2, 3),   # add +3 to submatrix (0,1)-(1,2)
]

# Apply range updates
delta = build_partial_2d(n, m, queries)
for i in range(n):
    for j in range(m):
        arr[i][j] += delta[i][j]

# Build prefix sum for fast queries
pref = build_prefix_2d(arr)

print("Updated grid:")
for row in arr:
    print(row)

# Example range sum query
print("Sum of submatrix (0,0)-(1,1):", range_sum_2d(pref, 0, 0, 1, 1))
