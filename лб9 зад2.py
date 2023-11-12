class Trapezoid:#определяем класс `Trapezoid`
    def __init__(self, a, b, c, d):#метод инициализирующий его атрибуты
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):#метод для расчета периметра трапеции
        return self.a + self.b + self.c + self.d
class Rhombus:#определяем класс `Rhombus`
    def __init__(self, a):#метод инициализирующий его атрибуты
        self.a = a

    def perimeter(self):#метод для расчета периметра ромба
        return 4 * self.a
class Rectangle:#определяем класс `Rectangle`
    def __init__(self, a, b):#метод инициализирующий его атрибуты
        self.a = a
        self.b = b
    def perimeter(self):#метод для расчета периметра круга
        return 2 * (self.a + self.b)
##экземпляры классов
trapezoid = Trapezoid(3, 6, 9, 6)
rhombus = Rhombus(7)
rectangle = Rectangle(5, 8)
##создание списка с экземплярами разных фигур
figures = [trapezoid, rhombus, rectangle]
for figure in figures:#цикл для прохода по списку и вывода площади каждой фигуры
    print("Периметр:", figure.perimeter())