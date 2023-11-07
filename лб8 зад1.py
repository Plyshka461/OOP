class Vector:
#создается список self.values, в который добавляются только те значения, которые являются целыми числами
    def __init__(self, *args):
        self.values=[]
        for n in args:
            if isinstance(n, int):
                self.values.append(n)
#возвращает строковое представление объекта Vector
    def __str__(self):
        if self.values:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'
v1=Vector(1,2,3)
print(v1)#печатает вектор(1,2,3)
v2=Vector()
print(v2)#Печатает пустой вектор