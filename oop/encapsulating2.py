import math

class TibetanSpaniel:
    family = "Ashraf Uddin"
    area_of_origin = 'Islam'
    learning_rate = 9
    obedience = 10
    problem_solving = 10

    def __init__(self, name, favorite_toy, watchdog_ability):
        self._name = name
        self.__favorite_toy = favorite_toy
        self.__watchdog_ability = watchdog_ability

    @property
    def name(self):
        return self.__favorite_toy
    
    @name.setter
    def name(self, x):
        self.__favorite_toy = x

    @property
    def watchdog_ability(self):
        return self.__watchdog_ability
    
    @watchdog_ability.setter
    def watchdog_ability(self, watchdog_ability):
        if watchdog_ability < 0:
            self.__watchdog_ability = 0
        elif watchdog_ability > 10:
            self.__watchdog_ability = 10
        else:
            self.__watchdog_ability = watchdog_ability
    
    @property
    def protection_score(self):
        return math.floor((self.__watchdog_ability + type(self).
        learning_rate + type(self).problem_solving) / 3)

object_tibetanspaniel = TibetanSpaniel('Ashraf', 'Nice', 12)


print(object_tibetanspaniel._name)
print(object_tibetanspaniel.name)

object_tibetanspaniel.name = 'Tamim'
print(object_tibetanspaniel.name)


print(object_tibetanspaniel.family)
object_tibetanspaniel.family = 'Tanjil Chowdhury'
print(object_tibetanspaniel.family)

print(object_tibetanspaniel.watchdog_ability)

object_tibetanspaniel.watchdog_ability = 12
print(object_tibetanspaniel.watchdog_ability)

print(object_tibetanspaniel.protection_score)

