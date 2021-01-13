class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('Ashraf', 200, 13)
car = Car('Tanjil', 300, 18)

print(bus.name, bus.max_speed, bus.mileage)
print(car.name, car.max_speed, car.mileage)