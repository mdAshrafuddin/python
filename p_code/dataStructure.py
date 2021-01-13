from collections import deque

# Stack defined here 
a = []
a.append('a')
a.append('b')
a.pop()
print(a)

# Queue here defiend

list = deque(['a', 'b'])
list.append('ab')
list.popleft()
print(list)

dic = {'name': "Ashraf", 'age': 20}

if 'name' in dic:
    print("true value", dic['name'])

list = []

for i in [1, 3, 5, 6]:
    list.append(i ** 2)
    print(f"{i} : {list}")


list1 = []

for i in [1, 2, 4, 6, 8]:
    for n in [2, 5, 1, 8]:
        if i != n:
            list1.append((i, n))
            print(list1)