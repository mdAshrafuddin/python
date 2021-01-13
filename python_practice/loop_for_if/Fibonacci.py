trems = 10
num1, num2 = 0, 1
count = 0

while count < trems:
    print(num1,end=' ')
    temp = num1 + num2
    num1 = num2
    num2 = temp
    count += 1

