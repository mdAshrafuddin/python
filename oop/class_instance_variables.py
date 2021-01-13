class Persion:
    # Class variable shared by all instances
    name = "Ashraf"

    def __init__(self, company, age):
        # instance variable unique to each instance
        self.company = company
        self.age     = age
    
x = Persion("ch company", 20)
print(f'Company name {x.company} and years {x.age}') # unique to d
print("=" * 30)
print(x.name) # Shared by all dogs
print(x.name) # Shared by all dogs

# 

# class Company:
#     # mistaken use of a class variable
#     tricks = []

#     def __init__(self, name, employee):
#         self.name = name
#         self.employee = employee
    
#     def add_trick(self, trick):
#         self.tricks.append(trick)
    
# x = Company("nice company", "Tanjil")
# print(f"Company name is {x.name} and employee name is  {x.employee}")
# x.add_trick("Ashraf")
# print(x.tricks)

# 

class Company:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    
x = Company("Ashraf")
print(x.name)
print("=" * 25)
x.add_trick("Ashraf")
x.add_trick("Tanjil")
print(x.tricks)