from collections import deque

list = deque(['a', 'b', 'c', 'd'])

list.append('q')
list.popleft()
print(list)

for i in range(10):
    print(i, i * i)