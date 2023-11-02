class Train:
    def __init__(self, city, train_number, start_time, total_seats, kup, plac):#инициализация полей
        self._city = city
        self._train_number = train_number
        self._start_time = start_time
        self._total_seats = total_seats
        self._kup = kup
        self._plac = plac
    @property
    def start_time(self):
        return self._start_time
    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def train_number(self):
        return self._train_number
    @train_number.setter
    def train_number(self, value):
        self._train_number = value
# Пример использования класса
train = Train('Forg', 12345, 3.25, 300, 100, 50)
# Получение значений через свойства
print('Номер поезда ', train.train_number)
print('Время прибытия ', train.start_time)
# Изменение значений через свойства
train.train_number = 54321
train.start_time = 5.38
# Вывод их
print('Новый номер поезда ', train.train_number)
print('Новое время прибытия ', train.start_time)