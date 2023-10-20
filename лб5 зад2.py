import math
class Vector:#Вводим класс
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def module(self):
        vector_module = math.sqrt(self.x ** 2 + self.y ** 2)
        return vector_module
    def multiply(self, k):
        multiplied_vector = Vector(k * self.x, k * self.y)
        return multiplied_vector
# Создание объекта класса Vector
vector = Vector(3, 4)
# Вызов метода module()
vector_module = vector.module()
print(f"|вектор| = {vector_module}, (f'|вектор| = {vector.x}^2 + {vector.y}^2')")
# Вызов метода multiply()
multiplied_vector = vector.multiply(2)
print(f"{2} * |вектор| = ({multiplied_vector.x}, {multiplied_vector.y}), (f'{2} * |вектор| = ({2} * {vector.x}, {2} * {vector.y})')")