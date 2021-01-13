# Defining class name
class Cat:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    # Create Info
    def info(self):
        return f'I am not cat,  He is {self.name} and he is {self.age} old'
    # Create make_sound
    def make_sound(self):
        print('Meow')
    
# Defining Class name
class Dog:
    # Constructor
    def __init__(self, name, age, id):
        self.name = name
        self.age  = age
        self.id = id
    
    # Create info
    def info(self):
        return f'I am not dog, He is {self.name} and he is {self.age} id {self.id}'
    
    def make_sound(self):
        print('Dog dog')


ob_dog = Dog('noo', 23, 3424)
print(ob_dog.info())