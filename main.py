"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь."""
import math
import random


class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def calc_len(self):
        return self.pi * self.radius * 2

    def calc_area(self):
        return self.pi * self.radius ** 2


a = Circle(12)
print(a.radius)
print(a.calc_area())
print(a.calc_len())


class Figure:

    def __init__(self, length_1, length_2=0):
        self.length_1 = length_1
        self.length_2 = length_1 if length_2 == 0 else length_2

    def calc_len(self):
        return (self.length_1 + self.length_2) * 2

    def calc_area(self):
        return self.length_1 * self.length_2


b = Figure(12, 14)
print(b.length_2)
print(b.calc_area())
print(b.calc_len())

"""Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f'{self.name} {self.surname}'


c = Person('Ivan', 'Maurin', 24)
print(c.get_age())
c.birthday()
print(c.get_age())
print(c.full_name())
print(c.__str__())


class Worker(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.id = random.randint(100000, 999999)
        self.level = sum(map(int, [x for x in str(self.id)])) % 7

    def __str__(self):
        return f'{self.name}, {self.id}, {self.level}'


d = Worker('Ivv', 'Agg', 22)
print(d)

"""Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса"""


class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f'{self.name} Говорит: '

    def birthday(self):
        self.age += 1


class Fish(Animals):
    def __init__(self, name, age, area='river', depth=10, weight=1):
        super().__init__(name, age)
        self.area = area
        self.depth = depth
        self.weight = weight

    def say(self):
        return super().say() + '...'

    def grow(self):
        self.weight *= 1.2
        self.depth *= 1.1


class Dog(Animals):
    def __init__(self, name, age, color='white', domestic=True):
        super().__init__(name, age)
        self.color = color
        self.domestic = domestic

    def say(self):
        return super().say() + 'Гав гав'

    @staticmethod
    def walk():
        return 'Минус одна спокойная кошка'


e = Dog('vv', 12, 'white')
r = Fish('dd', 1, 'ocean', 1200, 4)


class Factory:
    @staticmethod
    def create(obj_type, name, age, *args, **kwargs):
        try:
            match obj_type:
                case 'Dog':
                    return Dog(name, age, *args, **kwargs)
                case 'Fish':
                    return Fish(name, age, *args, **kwargs)
                case _:
                    raise ValueError('invalid class')
        except TypeError:
            print('ERROR arguments\nField init class')
            # exit()


task1 = Factory.create('Dog', 'Vil', 12, 'black', 123, 123, 123)
task1 = Factory.create('Dog', 'Vil', 12, 'black')
print(task1)
