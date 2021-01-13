# a = 334
# sum_digit = 0

# for digit in str(a):
#     sum_digit += int(digit)
# print(sum_digit)

a = int(input("Please Enter The Number: "))
sum = 0

# while a > 0:
for i in range(len(str(a))):
    digit = a % 10
    sum   = sum + digit
    a     = a // 10

print(sum)






