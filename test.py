from savana import *
import unittest
import pep8
import os

bear = Bear(10, 35)
cod = Cod(100, 1)
pinguin = Pinguin(15, 9)
seals = Seals(5, 8)


class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        filenames = []
        for root, _, files in os.walk('.'):
            if "venv" not in root:
                python_files = [f for f in files if f.endswith('.py')]
                for file in python_files:
                    filename = '{0}/{1}'.format(root, file)
                    filenames.append(filename)
        check = style.check_files(filenames)
        print(f'PEP8 style errors: {check.total_errors}')


class TestManager(unittest.TestCase):
    animals = [bear, cod, pinguin]
    savana = SavannaManager()
    savana.add_animals(animals)
    predators = savana.find_predators(1)

    def test_add_animals(self):
        self.assertEqual(self.savana.animals, self.animals)

    def test_add_animal(self):
        self.savana.add_animal(seals)
        self.animals.append(seals)
        self.assertEqual(self.savana.animals, self.animals)

    def test_find_predators(self):
        self.assertEqual(self.predators, [bear, pinguin])

    def test_sort_asc(self):
        sorted_predators = self.savana.sort_by_weight_of_food_consumed(self.predators, SortOrder.ASC)
        self.assertEqual(sorted_predators, [pinguin, bear])

    def test_sort_desc(self):
        sorted_predators = self.savana.sort_by_weight_of_food_consumed(self.predators, SortOrder.DESC)
        self.assertEqual(sorted_predators, [bear, pinguin])


class TestAnimalsStr(unittest.TestCase):
    def test_bear(self):
        self.assertEqual(str(bear), "Ведмідь - Тип живлення: Хижак,\
        Клас тварини: Ссавець,\
        Кілкість порібної їжі: 5,\
        Щвидкість бігу: 10 km/h,\
        Тривалість життя: 35")

    def test_cod(self):
        self.assertEqual(str(cod), "Тріска - Тип живлення: Всеїдний,\
        Клас тварини: Риба,\
        Кілкість порібної їжі: 2,\
        Щвидкість бігу: 100 km/h,\
        Тривалість життя: 1")

    def test_pinguin(self):
        self.assertEqual(str(pinguin), "Пінгвін - Тип живлення: Хижак,\
        Клас тварини: Птах,\
        Кілкість порібної їжі: 3,\
        Щвидкість бігу: 15 km/h,\
        Тривалість життя: 9")

    def test_seals(self):
        self.assertEqual(str(seals), "Тюлень - Тип живлення: Травоїдний,\
        Клас тварини: Ссавець,\
        Кілкість порібної їжі: 15,\
        Щвидкість бігу: 5 km/h,\
        Тривалість життя: 8")


if __name__ == '__main__':
    unittest.main()
