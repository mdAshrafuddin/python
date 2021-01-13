class Employee():
    def __init__(self, name, age, id, salary):
        self.id   = id
        self.name = name
        self.age  = age
        self.salary = salary

emp1 = Employee(2, 'Ashraf', 23, 300)
emp2 = Employee(3,"Tanjil", 24, 3000)

print(emp1.__dict__)
print(emp2.__dict__)