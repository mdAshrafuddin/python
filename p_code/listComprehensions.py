squares = []

for i in range(10):
    squares.append(i ** 2)
    print(squares[i], end=' ')

squares1 = list(map(lambda x: x ** 2, range(10)))
print(squares1, end=' ')

print([x ** 2 for x in range(10)])

coms = []
for x in [2, 4, 6, 8]:
    for y in [2, 4, 6, 5]:
        if x != y:
            coms.append((x, y))
print(coms, end=' ')

vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec if])
print([x for x in vec if x >= 0])
print([abs(n) for n in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

print([w.strip() for w in freshfruit])

print([(m, m ** 2) for m in range(6)])


