def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n-21) * 2
    

f = diff21(44)
print(f)