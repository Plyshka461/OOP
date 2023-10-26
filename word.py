#Создание класса
class Word:
    def __init__(self, word, page_numbers, total_pages):
        self.word = word
        self.page_numbers = page_numbers
        self.total_pages = total_pages
#Выводит информацию о слове
    def print_info(self):
        print(f"Слово: {self.word}")
        print(f"Номера страниц: {self.page_numbers}")
        print(f"Число страниц: {self.total_pages}")
#Возвращает количество страниц, на которых встречается слово
    def count_pages(self):
        return len(self.page_numbers)