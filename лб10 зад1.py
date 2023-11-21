class Transport:
    def __init__(self, brand, max_speed, kind=None):#инициализирует атрибуты объекта
        self.brand=brand
        self.max_speed=max_speed
        self.kind=kind
    def __str__(self):#возвращает строку, описывающую тип транспорта, марку и максимальную скорость
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):#вызывает конструктор родительского класса Transport и инициализирует дополнительные атрибуты объекта
        super().__init__(brand, max_speed, kind='Car')
        self.mileage=mileage
        self.__gasoline_residue=gasoline_residue
    @property
    def gasoline(self):#Метод является свойством и возвращает информацию о количестве остаточного бензина
        return f'Осталось бензина на {self.__gasoline_residue} км'
    @gasoline.setter#Метод является сеттером для установки значения остаточного бензина
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue+=value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')
class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):#вызывает конструктор родительского класса Transport и инициализирует атрибуты объекта
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name=owners_name
    def __str__(self):#возвращает строку, описывающую марку лодки и имя её владельца
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):#вызывает конструктор родительского класса Transport и инициализирует атрибуты объекта
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity=capacity
    def __str__(self):#возвращает строку, описывающую марку самолета и его вместимость
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#Пример использования
transport = Transport('Telega', 10)
print(transport)
bike = Transport('shkolnik', 20, 'bike')
print(bike)
first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)
first_car = Car('BMW', 230, 75000, 300)
print(first_car)
print(first_car.gasoline)
first_car.gasoline = 20
print(first_car.gasoline)
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)