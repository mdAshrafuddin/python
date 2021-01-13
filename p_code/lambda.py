print((lambda a, b : a + b)(2, 4))

def make_in(n):
    return lambda x : x + n

f = make_in(90)

print(f(78))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key= lambda pair:pair[1])
print(pairs)