from ..animal import *
import random


class Cod(Animal):
    def __init__(self, swimming_speed: int, life_time: int):
        self.swimming_speed = swimming_speed
        self.life_time = life_time
        super().__init__(FoodUsed.HERBIVOROUS, TypeOfAnimals.FISH, 2)

    def __str__(self):
        return f"Тріска - {super().__str__()}\
        Щвидкість бігу: {self.swimming_speed} km/h,\
        Тривалість життя: {self.life_time}"
