arr = [1, 2, 4, 4, 5, 6]
target = 5

""" lower bound 
    Find the first position where 'target' can be inserted
    (First from the left)
"""
print(" <==== Lower Bound ===>")
# 1.1 -> def 
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
# 1.2 using bisect  
from bisect import bisect_left

# Example usage:
idx1 = lower_bound(arr, target)
idx2 = bisect_left(arr, target)

print("Lower Bound Index (def):", idx1)  
print("Lower Bound Index (bisect):", idx2)

# ==============================================================
""" upper bound
    Find the last position where 'target' can be inserted
    (First from the right)
"""
print(" <==== Upper Bound ===>")
# 2.1 -> def 
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
# 2.2 using bisect 
from bisect import bisect_right

# Example usage:
idx3 = bisect_right(arr, target)
idx4 = upper_bound(arr, target)
print("Upper Bound Index (def):", idx4)  
print("Upper Bound Index (bisect):", idx3)  


# Search about Binary Search on Answer
# Codeforces Edu Section - (https://codeforces.com/edu/course/2/lesson/6/) (Recommended)
