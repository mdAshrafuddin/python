# A python program to demostrative inherative

class Persion(object):
    # Constructor
    def __init__(self, name):
        self.name = name 

    # To get name
    def get_name(self):
        return self.name

    # To Check if this persion is an employee
    def isEmployee(self):
        return False 
# Inherited or subclass
class Employee(Persion):
    def isEmployee(self):
        return True

emp = Persion("Geek1")
print(emp.get_name(), emp.isEmployee())
emp = Employee("Geek2")
print(emp.get_name(), emp.isEmployee())

# Other example inheritance
# A python program demostrative to inheritance 
class Add(object):
    # Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # To get add
    def get_add(self):
        return self.a + self.b 
    
    def isEmployee(self):
        return False

# Inheritance or sub class
class Sub(Add):
    def get_add(self):
        return self.a - self.b

    def isEmployee(self):
        return True

a = Add(2, 4)
print(a.get_add(), a.isEmployee())
b = Sub(4, 42)
print(b.get_add(), b.isEmployee())