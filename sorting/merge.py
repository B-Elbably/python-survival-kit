def merge_sort(arr):
    # Time : O(n log n)
    # Space: O(n)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    # while i < len(left):
    #     merged.append(left[i])
    #     i += 1

    merged.extend(right[j:])
    # while j < len(right):
    #     merged.append(right[j])
    #     j += 1
    return merged
