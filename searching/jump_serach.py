def jump_search(arr, target):
    """
    Time: O(√n)
    Space: O(1)
    Requires: Sorted array
    """
    n = len(arr)
    step = int(n**0.5)

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(jump_search(arr, 11))
