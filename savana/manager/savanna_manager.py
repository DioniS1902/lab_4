from ..animal import *


class SavannaManager:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def add_animals(self, animals: list):
        self.animals += animals

    def find_predators(self, min_number_of_meat: int):
        return [animal for animal in self.animals
                if animal > min_number_of_meat and animal.type_of_food_used is FoodUsed.PREDATOR]

    def sort_by_weight_of_food_consumed(self, animals: list, order: SortOrder):
        return sorted(animals, key=lambda x: x.number_of_food, reverse=order.value)
