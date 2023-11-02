# Определение класса A
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
# Определяем свойство c с помощью декоратора
    @property
    def c(self):
        return 3 * (self.a ** 3) + self.b
# Создание экземпляра класса A
obj = A(6, 9)
# Получение значения свойства c
result = obj.c
print(result)