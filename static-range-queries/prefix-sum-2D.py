def build_prefix_2D(matrix):
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    pref_2D = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            pref_2D[r][c] = (matrix[r - 1][c - 1] +
                                pref_2D[r - 1][c] +
                                pref_2D[r][c - 1] -
                                pref_2D[r - 1][c - 1])
    return pref_2D

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pref_2D = build_prefix_2D(matrix)
# print(pref_2D)  
for i in pref_2D:
    print(i)


# Search about List Comprehensions 
# if needed for simple matrix creation.