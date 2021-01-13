city = 'Dhaka'

for ch in city:
    print(ch, end=' ')

# define a list
my_list = [1, 2, 3, 4, 5, 6]

for x in my_list:
    for n in ('a', 'b', 'c', 'd'):
        print(x, n)

users = {
    'name':'Ashraf uddin',
    'age' : 23,
    'id'  : 23102004
}

for key, value in users.items():
    print(key, value)

for i in users.keys():
    print(i)

for i in users.values():
    print(i)

icity = iter(city)
print (icity.next())
print (icity.next())
print (icity.next())
print (icity.next())
print (icity.next())

