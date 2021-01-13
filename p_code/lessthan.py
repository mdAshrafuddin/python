a = [1, 3, 5, 7, 9, 33, 55, 89]

for n in a:
    if n > 5:
        print(n)

print('--'*10)
my_list = [1, 3, "Michele", [5, 6, 7]]

for n in my_list:
    print(n)
 
print('***'*10)

grade = int(input('Enter the grade: '))

if(grade >= 90):
    print('A')
elif(grade >= 80):
    print('A-')
elif (grade >= 70):
    print('B')
elif (grade >= 60):
    print('C')
elif (grade >= 40):
    print('D')
else:
    print('F')