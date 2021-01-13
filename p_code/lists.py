list = [1, 8, 3, 5, 6, 8, 9]
list1 = [1, 33, 55, 66]
n = list.extend(list1)
list.append(12)
list.insert(5, 20)
list.remove(6)
# list.clear()
# del list[:]
a = list.index(9)
b = list.count(8)
print(b)
print(a)
print(list)
print(n)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.pop()
print(fruits)
