from .constants import *

food_used = ["Всеїдний", "Хижак", "Травоїдний"]
animal_type = ["Птах", "Ссавець", "Риба"]


class Animal:
    def __init__(self, type_of_food_used: FoodUsed, type_of_animal: TypeOfAnimals, number_of_food: int):
        self.type_of_food_used = type_of_food_used
        self.type_of_animal = type_of_animal
        self.number_of_food = number_of_food

    def __gt__(self, other):
        return self.number_of_food > other

    def __str__(self):
        return f"Тип живлення: {food_used[self.type_of_food_used.value]},\
        Клас тварини: {animal_type[self.type_of_animal.value]},\
        Кілкість порібної їжі: {self.number_of_food},"
