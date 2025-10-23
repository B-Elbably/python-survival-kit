# Using Loop
def linear_search(arr, target):
    """
    Time Complexity: O(n)
    """
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


# Check if element exists
def check_exist(arr, target):
    """
    Time Complexity: O(n)
    """
    # return target in arr
    if target in arr:  # T.C: O(n) not O(1)
        return True
    return False


"""
    Search about this functions
    (min , max , sum)
    (count , index , pop(idx))
"""
