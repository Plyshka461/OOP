class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'  # Возвращает строку с информацией о человеке.

class Worker(Person):  # Наследуется от класса Person.
    def __init__(self, name, age, profession):
        super().__init__(name, age)  # Вызывает конструктор родительского класса.
        self.profession = profession

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Работа: {self.profession}'  # Возвращает строку с информацией о работнике.

class Father(Person):  # Наследуется от класса Person.
    def __init__(self, name, age, children=2):
        super().__init__(name, age)  # Вызывает конструктор родительского класса.
        self.children = children

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Кол. детей: {self.children}'  # Возвращает строку с информацией о отце.

class WorkingFather(Worker, Father):  # Наследуется от классов Worker и Father.
    def __init__(self, name, age, profession, children):
        Worker.__init__(self, name, age, profession)  # Вызывает конструктор класса Worker.
        Father.__init__(self, name, age, children)  # Вызывает конструктор класса Father.

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Работа: {self.profession}, Кол. детей: {self.children}'  # Возвращает строку с информацией о работающем отце.


person = Person('Архип', 46)
print(person)  # Выводит информацию о person.

worker = Worker('Сеня', 56, 'Актер')
print(worker)  # Выводит информацию о worker.

father = Father('Ваня', 34, 4)
print(father)  # Выводит информацию о father.

working_father = WorkingFather('Даник', 29, 'Работник зоопарка', 0)
print(working_father)  # Выводит информацию о working_father.
