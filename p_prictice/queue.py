from collections import deque

list = deque(['a','b'])

list.append('c')
list.popleft()
print(list)