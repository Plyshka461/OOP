import random
#Определение класса Flower
#Инициализация атрибутов
class Flower:
    def __init__(self, stem_length, freshness):
        self.stem_length=stem_length
        self.freshness=freshness
#Декораторы и соответствующие методы-сеттеры для атрибутов
    @property
    def stem_length(self):
        return self.__stem_length
    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            print('Длина должна быть числом')
        elif value < 5:
            print('Длина должна быть минимум 5')
        elif value > 20:
            print('Длина должна быть максимум 20')
        else:
            self.__stem_length=value
    @property
    def freshness(self):
        return self.__freshness
    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            print('Длина должна быть числом')
        elif value < 1:
            print('Длина должна быть минимум 1')
        elif value > 10:
            print('Длина должна быть максимум 10')
        else:
            self.__freshness = value
#Создание списка объектов класса Flower, для которых значения атрибутов-случайные чила
f=[]
for i in range(5):
    f.append(Flower(int(random.uniform(5, 20)),int(random.uniform(1, 10))))
    print(f'цветок {i+1}: длина стебля {f[i].stem_length}, уровень свежести {f[i].freshness}')
#сортировка списка объектов класса по атрибуту freshness (уровень свежести
result=sorted(f, key=Flower.freshness.fget)
#вывод элементов отсортированного списка
print('Отсортированный букет:')
for i in range(5):
    print(f'цветок {i+1}-уровень свежести {result[i].freshness}')
#задание диапазона длин стеблей
l1=int(input('введите начальное значение диапазона'))
l2=int(input('введите конечное значение диапазона'))
#вывод элементов списка заданного диапазона
for i in range(5):
    if f[i].stem_length >=11 and f[i].stem_length <=12:
        print(f'цветок {i+1}-длина стебля {f[i].stem_length}')