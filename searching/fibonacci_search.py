def fibonacci_search(arr, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0 if arr[0] == target else -1

    fib0 = 0
    fib1 = 1
    fib2 = fib0 + fib1

    while fib2 < n:
        fib0 = fib1
        fib1 = fib2
        fib2 = fib0 + fib1

    offset = -1

    while fib2 > 1:
        i = min(offset + fib0, n - 1)

        # one step down
        if arr[i] < target:
            fib2 = fib1
            fib1 = fib0
            fib0 = fib2 - fib1
            offset = i
        # two steps down
        elif arr[i] > target:
            fib2 = fib0
            fib1 = fib1 - fib0
            fib0 = fib2 - fib1
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    return -1


# Learn more about Fibonacci (بكلمك بجد)
