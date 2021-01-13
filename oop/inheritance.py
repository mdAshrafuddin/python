class Animal:
    _number_of_legs = 0
    _pairs_of_eyes = 0

    def __init__(self, age):
        self._age = age
        print('Animal Printed')

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

    def print_legs_eyes(self):
        print("I have " + str(self._number_of_legs) + "legs and "+ (self._pairs_of_eyes * 2))
    
    def print_age(self):
        print("I am " + str(self._age) + "Years old")

class Mammal(Animal):
    _pairs_of_eyes = 1

    def __init__(self, age, is_pragnat=False):
        super().__init__(age)
        self._is_pragnat = is_pragnat

    @property
    def is_pragnat(self):
        return self._is_pragnat

    @is_pragnat.setter
    def is_pragnat(self, is_pragnat):
        self._is_pragnat = is_pragnat


# ob_mammal = Mammal(23, True)
# print(ob_mammal.is_pragnat)
# print(ob_mammal.age)

# Overriding methods

class DomesticMammal(Mammal):
    def __init__(self, name, age, favorite_toy, is_pregnant=False):
        super().__init__(age, is_pregnant)
        self._name = name
        self._favorite_toy = favorite_toy
        self._is_pregnant = is_pregnant

    @property
    def name(self):
        return self.name
    
    @property
    def favorite_toy(self):
        return self.favorite_toy
    @favorite_toy.setter
    def favorite_toy(self, favorite_toy):
        self.favorite_toy = favorite_toy
    
    def talk(self):
        print(self._name + ": talks")


class Dog(DomesticMammal):
    _number_of_legs = 4
    _breed = "Just a dog"
    _breed_family = "Dog"

    def __init__(self, name, age, favorite_toy, is_pragnat = False):
        super().__init__(name, age, favorite_toy, is_pragnat)
        print("Dog created")
    
    def bark(self, times=1, other_domestic_mammal=None, is_angry=False):
        message = self.name

        if other_domestic_mammal is not None:
  1          message += " to " + other_domestic_mammal.name + ": "
        else:
            message += ':'

        if is_angry:
            message += 'Grr'

            message += 'Woof ' * times
            print(message)
    
    def talk(self):
        self.bark()

    @classmethod
    def print_method(cls):
        print(cls._breed)

    @classmethod
    def print_breed_family(cls):
        print(cls._breed_family)

# class TerrierDog(Dog):
#     _breed = "Terrier dog"
#     _breed_family = "Terrier"
#     def __init__(self, name, age, favorite_toy, is_pregnant=False):
#         super().__init__(name, age, favorite_toy, is_pregnant)
#         print("TerrierDog created")

# class SmoothFoxTerrier(TerrierDog):
#     _breed = "Smooth Fox Terrier"
#     def __init__(self, name, age, favorite_toy, is_pregnant=False):
#         super().__init__(name, age, favorite_toy, is_pregnant)
#         print("SmoothFoxTerrier created")


ob_dog = Dog()

print(ob_dog.talk())