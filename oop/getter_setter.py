class Student:
    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name
    
    def set_marks(self, m):
        self.m = m
    
    def get_marks(self):
        return self.m

    def dispaly(self):
        print('Name: ', self.name)
        print('Marks: ', self.m)

s = Student()
s.set_name("Ashraf")
s.set_marks(2.3)
print(s.dispaly())

