class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age  = age
        self.id   = id
    
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


    def getName(self):
        return '{0} {1} {2}'. format(self.name, self.age, self.id)




class Student_child(Student):
    def __init__(self, name, age, id, email):
        super().__init__(name, age, id)
        self.email = email

    def getName(self):
        return '{0} {1} {2} {3}'. format(self.name, self.age, self.id, self.email)



ob_class = Student('Ashraf', 23, 2364)

print(ob_class.getName())

ob_child = Student_child('Ashraf', 23, 2364, 'asshraf@gmail.com')
print(ob_child.getName())
