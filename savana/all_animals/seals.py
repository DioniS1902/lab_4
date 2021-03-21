from ..animal import *
import random


class Seals(Animal):
    def __init__(self, swimming_speed: int, life_time: int):
        self.swimming_speed = swimming_speed
        self.life_time = life_time
        super().__init__(FoodUsed.OMNIVOROUS, TypeOfAnimals.MAMMALS, 15)

    def __str__(self):
        return f"Тюлень - {super().__str__()}\
        Щвидкість бігу: {self.swimming_speed} km/h,\
        Тривалість життя: {self.life_time}"
