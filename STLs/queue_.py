# NOTE: Dont name file as queue.py 

from queue import Queue

q = Queue(maxsize=3)
q.put(10)
q.put(20)
q.put(15)

# q.put(25)  # ⚠️ This will wait forever!

try:
    q.put_nowait(25)  # ❌ Raises queue.Full
except:
    print("Queue is full! Can't add 25")

print("Get:", q.get())           # 10 (removes and returns - FIFO)
print("Get nowait:", q.get_nowait())  # 20
print("Get:", q.get())           # 15

# q.get()  # ⚠️ This will wait forever!

try:
    q.get_nowait()  # ❌ Raises queue.Empty
except:
    print("Queue is empty!")
    
    
    
# 2- Use List & pop(0) (Not Recommend - O(n) time complexity)
# 3- Use collections.deque (Recommend)