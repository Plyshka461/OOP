class Quadrilateral:
#метод инициализирует объект
    def __init__(self, *args):
        if len(args) == 1:#если количество аргументов равно 1
            #то устанавливает ширину и высоту равными этому значению
            self.width = args[0]
            self.height = args[0]
        elif len(args) == 2:#Если количество аргументов равно 2
            #то устанавливает ширину и высоту равными этим двум значениям
            self.width = args[0]
            self.height = args[1]
#метод возвращает строковое представление объекта
    def __str__(self):
        if self.width == self.height:#Если ширина равна высоте
            return f"Квадрат размером {self.width}х{self.height}"#вывод информации о квадрате
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"#о прямоугольнике
#метод возвращает истину
    def __bool__(self):
        #если ширина равна высоте, и ложь в противном случае
        return self.width == self.height
# Создание квадрата
square = Quadrilateral(5)
print(square)
print(bool(square))
# Создание прямоугольника
rectangle = Quadrilateral(4, 6)
print(rectangle)
print(bool(rectangle))