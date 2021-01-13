for i in range(2, 10):
    for n in range(2, i):
        if i % n == 0:
            print(i, "Equals", n, '*', i // n)
            break
    else:
        print(i, 'is prime number')

for i in range(2, 10):
        if i % 2 == 0:
            print(i, "prime number")
            continue
        else:
            print(i, 'odd number') 

