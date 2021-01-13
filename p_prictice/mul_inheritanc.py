class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
class Employee1():
    def __init__(self, name, age, salary):
        self.name = name
        self.age  = age
        self.salary = salary

class ChildEmployee(Employee, Employee1):
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age  = age
        self.salary = salary
        self.id = id

em = Employee("Ashraf", 22)
print(em.name, em.age)
em1 = Employee1("Ashraf", 22, 3323)
print(em1.name, em1.age, em1.salary)

em2 = ChildEmployee("Ashraf", 22, 3323, 8)
print(em2.name, em2.age, em2.salary, em2.id)