class Rectangle:#класс 'Прямоугольник'
    def __init__(self,a ,b):#метод инициализирующий его атрибуты
        self.a=a
        self.b=b
    def get_area(self):#метод для расчета площади прямоугольника
        return self.a*self.b
class Square:#класс 'Квадрат'
    def __init__(self, a):#метод для инициализации стороны
        self.a=a
    def get_area(self):#метод для расчета площади квадрата
        return self.a**2
class Circle:#класс 'Круг'
    def __init__(self, r):#метод init для инициализации радиуса
        self.r=r
    def get_area(self):#метод для расчета площади круга
        return 3.14*self.r**2
#экземпляры классов
rect1=Rectangle(3,4)
rect2=Rectangle(12,3)
#print(rectl.get_rect_area(), rect2.get_rect_area())
sql=Square(2)
#print (sql.get_sq_area())
cirl=Circle(3)
#создание списка с экземплярами разных фигур
figure=[rect1, rect2, sql, cirl]
for figure in figure:#цикл для прохода по списку и вывода площади каждой фигуры
    print(figure.get_area())