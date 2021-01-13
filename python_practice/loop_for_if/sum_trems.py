number_of_terms = 5
start = 2
sum = 0

for n in range(1, number_of_terms+1):
    print(start, end='+')
    sum = sum + start
    start = (start * 10) + 2
print('\nsum above series is of:', sum)

