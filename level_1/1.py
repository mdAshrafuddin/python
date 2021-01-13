l = []

for i in range(100, 500):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

print(','.join(l))