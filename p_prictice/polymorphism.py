class cat():
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def info(self):
        print(f"My name is {self.name} and years {self.age} olds")
    
    def make_sound(self):
        print('Meow')

class dog():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def info(self):
        print(f"My name is {self.name} and years {self.age} olds")

    def make_sound(self):
        print('Geow')

c = cat("Tanjil", 34)
d = dog("Ashraf", 23)

for x in (c, d):
    x.make_sound()
    x.info()
    x.make_sound()