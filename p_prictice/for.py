list = [1, 3, 5, 7, 9, 92]

for x in list:
    print(x)

for n in range(10):
    print(n)

a = ['a', 'b', 'c']
b = []

for x in a:
    b.append(a)
    print(x)

print("ENter the number: ")

listNum = 6

for x in range(1, listNum):
    for y in range(1, x+1):
        print(y, end=' ') 
    print("")

n =2

for i in range(1, 11):
    p = n ** i
    print(p)