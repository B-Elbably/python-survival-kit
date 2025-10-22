# 1- Use dq from collections 
from collections import deque

"""
    append , appendleft -> O(1)
    pop , popleft -> O(1)
    extend , extendleft -> O(k) , k is length 
"""
dq = deque()
dq.append(10)          # deque([10])
dq.append(20)          # deque([10, 20])

# Append to left (unique to deque)
dq.appendleft(5)       # deque([5, 10, 20])
dq.appendleft(1)       # deque([1, 5, 10, 20])

# Add multiple elements (pythonic way)
dq.extend([30, 40])    # deque([1, 5, 10, 20, 30, 40])
dq.extendleft([0, -1]) # deque([-1, 0, 1, 5, 10, 20, 30, 40])

back = dq.pop()  # like stack        # 40, deque([-1, 0, 1, 5, 10, 20, 30])
front = dq.popleft() # like queue     # -1, deque([0, 1, 5, 10, 20, 30])

print(dq)
print(list(dq))  


