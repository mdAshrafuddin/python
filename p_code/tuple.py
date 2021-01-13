import sys

# a = (1, 'm')

# # if 'm' in a:
# #     print("m is true")
# # else:
# #     print("Not value")


# try:
#     a.append(2)
#     print(a)
# except AttributeError:
#     print("Error: Attribute Error")
#     sys.exit(1)

t = ((1, 3, 5, 6), (1, 2, 4, 66))
# n = len(t)
print(t)

try:
    v = ([1, 3, 5], [3, 5, 7])
    v.append(3)
    print(v)
except AttributeError:
    print('Error: AttributeError')
    sys.exit(1)
