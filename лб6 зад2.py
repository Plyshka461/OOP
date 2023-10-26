import random#Ввод рандома
#Создание класса Student с атрибутами
class Student:
    def __init__(self, name, group_number, academic_perfomance):
        self.name = name
        self.group_number = group_number
        self.academic_perfomance = academic_perfomance
        self.gpa_scores = sum(self.academic_perfomance) / 5
#Вывод информации о студенте на экран
    def print_info(self):
        print(f'ФИ: {self.name}\n'
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_perfomance}\n'
              f'  Средний балл: {self.gpa_scores}\n')
#Определяем ключ сортировки
def byGPA_key(person):
    return person.gpa_scores
#Создание списка из 10 студентов
students = [
    Student(input('Введите фамилию и имя студента: '),
        input('Введите номер группы: '),
        [random.randint(1, 10) for i_grade in range(5)])
    for i_student in range(10)]
#Сортируем список по среднему баллу
students_sort = sorted(students, key = byGPA_key)
#Вывод информации о каждом студенте
for student in students_sort:
    student.print_info()
