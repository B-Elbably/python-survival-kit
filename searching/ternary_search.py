def ternary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while hi - lo >= 3:
        mid1 = lo + (hi - lo) // 3
        mid2 = hi - (hi - lo) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            hi = mid1 - 1
        elif target > arr[mid2]:
            lo = mid2 + 1
        else:  # arr[mid1] <= target <= arr[mid2]
            lo = mid1 + 1
            hi = mid2 - 1

    for i in range(lo, hi + 1):
        if arr[i] == target:
            return i
    return -1


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
idx = ternary_search(arr, target)
if idx == -1:
    print("Not found")
else:
    print("Found at index: ", idx)


# Solve some problems using ternary search
# Leetcode: https://leetcode.com/problems/
