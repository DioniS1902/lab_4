from enum import Enum


class SortOrder(Enum):
    ASC = 0
    DESC = 1


class FoodUsed(Enum):
    HERBIVOROUS = 0
    PREDATOR = 1
    OMNIVOROUS = 2


class TypeOfAnimals(Enum):
    BIRD = 0
    MAMMALS = 1
    FISH = 2
