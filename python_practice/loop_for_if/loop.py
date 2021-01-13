list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for n in list1:
    if n > 150:
        break
    elif n % 5 == 0:
        print(n)
        