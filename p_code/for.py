# # for target_list in expression_list: suite
# # [else:suite]

# # n = [1, 3, 5, 6]

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# # # string, tuple or list
# # persion = ["AShraf", 'tanjil', 'tamim', 'asj']

# # for p in persion:
# #     print(p, len(p))

# phone_book = {
#     "Mom": "123-44-55-665",
#     "Dad": "233-33-55"
# }

# print(phone_book['Mom'])

# # users = {
# #     "Ashraf": "inactive",
# #     "Tanjil": "active",
# #     "tamim" : "active"
# # }

# # for user, status in users.copy().items():
# #     if status == 'inactive':
# #         del users[user]

# # print("After deleting users")
# # for user, status in users.items():
# #     print(user, status)
    
# # users = {
# #     "John": "inactive", 
# #     "Helen": "active",
# #     "James": "active", # and so on...
# # }

# # for user, status in users.copy().items():
# #     if status == 'inactive':
# #         del users[user]

# # print('After deleting users')

# # for user, status in users.copy().items():
# #     print(user, status)



# users = {
#     "John": "inactive", 
#     "Helen": "active",
#     "James": "active", # and so on...
# }

# # active_users = {}


# # for user, status in users.items():
# #     if status == 'active':
# #         active_users[user] = status
    
# # for user, status in active_users.items():
# #     print(user, status)

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
    
# for user, status in users.copy().items():
#     print(user, status)

# print(sum(range(1, 10, 5)))

list = ['Ashraf', 'Tanjil', 'Tamim Chowdhury']

for i in list:
    print(i, len(i))

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i, v in enumerate(a):
    print(i, v)

dic = {'name':'Ashrav', 'age':20}

for k, v in dic.items():
    print(k,v) 
