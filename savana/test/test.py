from ..all_animals import *
from ..manager import *


class Test:
    def __init__(self):
        self.savana = SavannaManager()
        self.savana.add_animals([Bear(10, 35), Cod(100, 1), Pinguin(15, 9), Seals(5, 8)])

    def test_print(self):
        print("Тест виводу")
        [print(animal) for animal in self.savana.animals]

    def test_sort(self):
        animals = self.savana.find_predators(1)
        sorted_animals = self.savana.sort_by_weight_of_food_consumed(animals, SortOrder.ASC)
        print("\nТест сортування")
        [print(animal) for animal in sorted_animals]

        reverse_sorted_animals = self.savana.sort_by_weight_of_food_consumed(animals, SortOrder.DESC)
        print("\nЗворотний тест сортування")
        [print(animal) for animal in reverse_sorted_animals]
