num = 5
fec = 1

if num < 0:
    print('Factorial does not exist for negtive number')
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for n in range(1,num+1,1):
        fec = fec * n
    print('The factrorial of ', num, 'of', fec)