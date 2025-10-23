def selection_sort(arr):
    # Time: O(n^2)
    # Space: O(1)
    n = len(arr)
    for i in range(n):
        pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]
    return arr


arr = list(map(int, input().split()))
print(selection_sort(arr))
