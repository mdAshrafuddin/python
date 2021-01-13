class Developer:
    def __init__(self, name, salary, age, companyName):
        self.name = name
        self.salary = salary
        self.age = age
        self.companyName = companyName

    @property
    def company(self):
        return self.companyName

    @company.setter
    def company(self, companyName):
        self.companyName = companyName


object_developer = Developer('Ashraf', 2300, 23, 'Ashraf Company')
print(object_developer.company)
object_developer.companyName = "Tanjil Chowdury"
print(object_developer.companyName)