# def fib(n):

#     a = 0
#     b = 1
#     if n == 1:
#         print(a)

#     else: 
#         print(a)
#         print(b)

#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)

# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result

# f100 = fib2(100)    # call it
# print(f100)              # write the result


def fib(n):
    a = 0
    b = 1

    for i in range(2, n):
        c = a + b # 0 + 1 = 1, 1 + 1 = 2, 2 + 1= 3
        a = b     # 2  
        b = c     # 3  
        print(c)
fib(10)

i = 5

def f(arg=i):
    print(arg)

i = 6
f()