# 1- Use module queue.priorityqueue
from queue import PriorityQueue

pq = PriorityQueue()
# pq.put((priority, actual_data))
pq.put((2, "Medium important task"))
pq.put((1, "Important task"))
pq.put((3, "Least important task"))
pq.put((0, "Most important task"))
# pq.put((-1, "task 1b")) # negative priorities are valid
print(" <==== Priority Queue ===>")
while not pq.empty():
    priority, task = pq.get()
    print(f"{priority}: {task}")


# 2- Use Heap (Recommend for problem solving)
import heapq

heap = []
heapq.heappush(heap, (2, "Medium important task"))
heapq.heappush(heap, (1, "Important task"))
heapq.heappush(heap, (3, "Least important task"))
heapq.heappush(heap, (0, "Most important task"))
# heapq.heappush(heap, (-1, "task 1b")) # negative priorities are valid
print(" <==== Heap ===>")
while heap:
    priority, task = heapq.heappop(heap)
    print(f"{priority}: {task}")

# Note: Search about difference between Heap & Priority Queue
# Not the same in all aspects
