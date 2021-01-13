# class InputOutPut(object):
#     def __init__(self):
#         self.x = ""

#     def getString(self):
#         self.x = input()

#     def outPutString(self):
#         print (self.x.upper())


# x = InputOutPut()

# print(x.getString())
# print(x.outPutString())

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    False

x = sleep_in(10,0)
print(x)