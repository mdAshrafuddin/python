dict = {'a':23, 'b':33}
dict['color'] = 'ASHRAF' 
for x in dict.values():
    print(x)
# mydict = dict.copy()
# print(len(mydict))
# for x,y in dict.items():
#     print(x,y)

# if 'a' in dict:
#     print('Yes')
# else:
#     print('No')

# vec = [-4, -2, 0, 2, 4]
# print([abs(x) for x in vec if x >= 0])

print([(x, x*2) for x in range(6)])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

print([x.strip() for x in freshfruit])

vec = [[1,2,3], [4,5,6], [7,8,9]]

print([x for x in vec for x in vec])

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[:]

print(a)