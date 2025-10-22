# TODO: Formal Implementation of Quick Sort
def quick_sort(arr, low, high):
    # Time: O(n log n) average, O(n²) worst
    # Space: O(log n) average, O(n) worst
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    # Time: O(n) for each partition
    # Space: O(1)
    # print("New partition call on:", arr[low:high+1])
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        # print(f"  Comparing arr[{j}]={arr[j]} with pivot={pivot}: ", arr[low:high+1])
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ===========================================================
# pythonic quick sort (not in place)
def quick_sort_py(arr):
    # Time: O(n log n) average, O(n²) worst
    # Space: O(n) average, O(n) worst
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_py(left) + middle + quick_sort_py(right)




arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Before sorting 1 :", arr)
sorted1 = quick_sort(arr.copy(), 0, n - 1)
print("After sorting 1  :", sorted1)

print("Before sorting 2 :", arr)
sorted2 = quick_sort_py(arr.copy())
print("After sorting 2  :", sorted2)
# N^2 if already sorted and last element is always chosen as pivot