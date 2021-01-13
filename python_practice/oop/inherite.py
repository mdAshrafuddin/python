class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


obBus = Bus('Ashraf', 120, 12)
print('Nam is', obBus.name, 'max speed', obBus.max_speed, 'mileage', obBus.mileage)