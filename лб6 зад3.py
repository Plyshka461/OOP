from word import Word
# Создание массива объектов класса Word
words = [
    Word("mahinka", [1, 3, 5], 10),
    Word("kukolka", [2, 4, 6], 10),
    Word("karti", [1, 2, 3, 4], 10),
    Word("pistoletik", [2, 4, 6, 8], 10),
    Word("miacik", [1, 3, 5, 7, 9], 10)]
# Вывод слов, которые встречаются на более чем N страницах
N = 3
for word in words:
    if word.count_pages() > N:
        word.print_info()