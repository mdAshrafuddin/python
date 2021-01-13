# # take user input number

# start = int(input("Enter the minimum Number: "))
# end   = int(input("Enter the maximum Number: "))

# for i in range(start, end):
#     if i > 1:
#         for j in range(2, i):
#             if (i % j == 0):
#                 break
#     else:
#         print(i)

# Python Program to print Prime Numbers from 1 to 100
 
# for Number in range (1, 101):
#     count = 0
#     for i in range(2, (Number//2 + 1)):
#         if(Number % i == 0):
#             count = count + 1
#             break

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')


# formula 4
num = int(input("Enter input number whether prime or not prime"))

if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "Not prime number")
        else:
            print(num, "Prime number")

else:
    print(num, "Not prime number")