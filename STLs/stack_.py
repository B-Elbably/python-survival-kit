# NOTE: Dont name file as queue.py 

# 1- Use module 
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
stack.put(10)
stack.put(20)
stack.put(15)

# stack.put(25)  # ⚠️ This will wait forever!

try:
    stack.put_nowait(25)  # ❌ Raises queue.Full
except:
    print("Stack is full! Can't add 25")

print("Get:", stack.get())           # 15 (removes and returns)
print("Get nowait:", stack.get_nowait())  # 20
print("Get:", stack.get())           # 10

# stack.get()  # ⚠️ This will wait forever!

try:
    stack.get_nowait()  # ❌ Raises queue.Empty
except:
    print("Stack is empty!")



# 2- Use List (Recommend)
stack = []
stack.append(10)
stack.append(20)
print("Stack after pushes:", stack)
top = stack.pop() # remove & return at the same time
print("Stack after pop:", stack)
