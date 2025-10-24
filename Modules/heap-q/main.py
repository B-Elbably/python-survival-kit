# 1- Min Heap -> default heap (min at root)
print(" <==== Min Heap ===>")
import heapq

nums = [5, 2, 7, 1, 3]
heapq.heapify(nums)  # O(n), build heap
print(nums)

# pop all elements in sorted order
sorted_nums = [heapq.heappop(nums) for _ in range(len(nums))]  # O(n log n)
print(sorted_nums)


# 2- Max Heap -> use negative values
print("\n <==== Max Heap ===>")
nums = [5, 2, 7, 1, 3]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)  # O(n)
heapq.heappush(max_heap, -10)  # O(log n)
max_val = -heapq.heappop(max_heap)  # O(log n)
print(max_val, [-n for n in max_heap])


# 3- Heapify -> build heap from list
print("\n <==== Heapify ===>")
nums = [9, 4, 7, 1, 6]
heapq.heapify(nums)  # O(n)
print(nums)


# 4- heappushpop -> push then pop smallest in one op
print("\n <==== heappushpop ===>")
nums = [2, 5, 7]
val = heapq.heappushpop(nums, 1)  # O(log n)
print(val, nums)


# 5- heapreplace -> pop smallest then push new value
print("\n <==== heapreplace ===>")
nums = [2, 5, 7]
val = heapq.heapreplace(nums, 1)  # O(log n)
print(val, nums)


# 6- nsmallest / nlargest -> get k smallest/largest
print("\n <==== nsmallest / nlargest ===>")
nums = [5, 2, 7, 1, 3]
print(heapq.nsmallest(3, nums))  # O(n log k)
print(heapq.nlargest(2, nums))   # O(n log k)


# 7- merge -> merge multiple sorted iterables
print("\n <==== merge ===>")
a = [1, 4, 6]
b = [2, 3, 5]
merged = heapq.merge(a, b)  # O(n), returns iterator
print(list(merged))
