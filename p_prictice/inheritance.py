class Employee1():
    def __init__(self, name, age, salary):
        self.name = name
        self.age  = age
        self.salary = salary
    

class ChildEmployee(Employee1):
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age  = age
        self.salary = salary
        self.id     = id

class ChildEmployee1(ChildEmployee):
    def __init__(self, name, age, salary, id, address):
        self.name = name
        self.age  = age
        self.salary = salary
        self.id     = id
        self.address = address

ch = Employee1("Ashraf", 22, 200)
print(f'My name is {ch.name} age {ch.age} salary {ch.salary}')
ch1 = ChildEmployee('Tanjil', 23, 2002, 1)
print(f'My name is {ch1.name} age {ch1.age} salary {ch1.salary} id {ch1.id}')
chE = ChildEmployee1('Tanjil', 23, 2002, 1, 'Habiganj')
print(f'My name is {chE.name} age {chE.age} salary {chE.salary} id {chE.id} address {chE.address}')