year = 2020
event = 'Ashraf'
print(f'Results of the {year} {event}')

# other exmaple
yes_votes = 42_23_12_45
no_votes   = 43_223_22_33

percentge = yes_votes / (yes_votes + no_votes)
print('{:-4} YES votes {:2.2%}'.format(yes_votes, percentge))


s = 'Hello world\n'

print(repr(s))

s = str('1 + 3')

print(repr(s))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for n, m in table.items():
    print(f'{n:10} =============>>> {m:10}')

animals = 'Tanjil'

print(f'My hovercraft is full of {animals}.')

print('{0} and {1} {2}'.format('spam', 'eggs', 'ashraf'))

print('{food} {aadjective}'.format(food = 'spam', aadjective = 'Absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

for x in range(1, 11):
    print('{0:d} {1:3d} {2:3d}'. format(x, x*x, x*x*x))

