class Student:
    def init (self, name, group, grades):#
        self.name = name
        self.group = group
        self.grades = grades
        # Метод для печати информации о студенте, выводит на экран имя, номер группы и успеваемость.
    def print_info(self):
        print(f"Студент: {self.name}")
        print(f"Номер группы: {self.group}")
        print(f"Успеваемость: {self.grades}")
students = []
#Цикл для ввода информации о 10 студентах
for _ in range(10):
    name = input("Введите ФИ студента: ")
    group = input("Введите номер группы: ")
    grades = []
## Цикл для ввода оценок за 5 предметов
    for i in range(5):
        grade = float(input(f"Введите оценку за предмет {i+1}: "))
        grades.append(grade)
# Создание объекта Student и добавление его в список
    student = Student(name, group, grades)
    students.append(student)
#Сортировка списка студентов по возрастанию среднего балла
students.sort(key=lambda student: sum(student.grades) / len(student.grades))# Сортировка студентов по увелечению среднего балла
for student in students:# Вывод информации о студентах
    student.print_info()
    print()