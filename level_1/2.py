def func(x):
    if x == 0:
        return 1
    return x * func(x-1)

n = func(5)
print(n)