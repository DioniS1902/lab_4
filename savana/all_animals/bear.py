from ..animal import *
import random


class Bear(Animal):
    def __init__(self, run_speed: int, life_time: int):
        self.run_speed = run_speed
        self.life_time = life_time
        super().__init__(FoodUsed.PREDATOR, TypeOfAnimals.MAMMALS, 5)

    def __str__(self):
        return f"Ведмідь - {super().__str__()}\
        Щвидкість бігу: {self.run_speed} km/h,\
        Тривалість життя: {self.life_time}"
