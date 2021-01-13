# Python program to
# Demonstrate queue implementaion
# using collection dequeue
from collections import deque

deque = deque()

# initializing a queue
deque.append("a")
deque.append("b")
deque.append("c")
print(deque)

# Removing elements from a queue

print("Removing elements from a queue") 
deque.popleft()
deque.popleft()
print(deque)