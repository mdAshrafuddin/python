class TibetanSpaniel:
    family = "Ashraf Uddin"
    area_of_origin = 'Islam'
    learning_rate = 9
    obedience = 10
    problem_solving = 10

    def __init__(self, name, favorite_toy, watchdog_ability):
        self.name = name
        self.favorite_toy = favorite_toy
        self.watchdog_ability = watchdog_ability


object_tibetanspaniel = TibetanSpaniel('Ashraf', 'Nice', 23)

print(object_tibetanspaniel.name)
print(object_tibetanspaniel.family)
object_tibetanspaniel.family = 'Tanjil Chowdhury'
print(object_tibetanspaniel.family)
