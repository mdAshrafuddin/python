def outerFun(a,b):
    def innerFun(a,b):
        return a+b
    add = innerFun(a,b)
    return add+5

outer = outerFun(30,20)
print(outer)
    