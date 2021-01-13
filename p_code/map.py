def myFun(x):
    return x * x

num = [1, 3, 5, 7]

result = list(map(myFun, num))
print(result)