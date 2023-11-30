class Collection:
    def __init__(self):#Класс представляет коллекцию и имеет два свойства
        self._name = ""
        self._owner_name = ""
    @property
    def name(self):#Метод является свойством и возвращает информацию названия
        return self._name
    @name.setter#Метод является сеттером для установки значения
    def name(self, value):
        self._name = value
    @property
    def owner_name(self):#Метод является свойством и возвращает информацию о имени создателя
        return self._owner_name
    @owner_name.setter#Метод является сеттером для установки значения имени создателя
    def owner_name(self, value):
        self._owner_name = value
class MusicalCarrier:
    def __init__(self):#Класс представляет музыкальный носитель и имеет четыре свойства
        self._author = ""
        self._genre = ""
        self._release_year = 0
        self._total_duration = 0
    @property#Метод является свойством и возвращает информацию названия автора
    def author(self):
        return self._author
    @author.setter#Метод является сеттером для установки значения автора
    def author(self, value):
        self._author = value
    @property#Метод является свойством и возвращает информацию названия жанра
    def genre(self):
        return self._genre
    @genre.setter#Метод является сеттером для установки значения жанра
    def genre(self, value):
        self._genre = value
    @property#Метод является свойством и возвращает информацию даты выхода
    def release_year(self):
        return self._release_year
    @release_year.setter#Метод является сеттером для установки даты выхода
    def release_year(self, value):
        self._release_year = value
    @property#Метод является свойством и возвращает информацию об общей длительности
    def total_duration(self):
        return self._total_duration
    @total_duration.setter#Метод является сеттером для установки общей длительности
    def total_duration(self, value):
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._total_duration = value
class MusicalComposition:#Класс представляет музыкальное произведение и имеет два свойства
    def __init__(self):
        self._name = ""
        self._duration = 0
    @property#Метод является свойством и возвращает информацию о названии
    def name(self):
        return self._name
    @name.setter#Метод является сеттером для установки названия
    def name(self, value):
        self._name = value
    @property#Метод является свойством и возвращает информацию продолжительности
    def duration(self):
        return self._duration
    @duration.setter#Метод является сеттером для установки продолжительности
    def duration(self, value):
        self._duration = value
class Song(MusicalComposition):#Класс наследуется от класса MusicalComposition и добавляет два дополнительных свойства
    def __init__(self):
        super().__init__()
        self._lyrics = ""
        self._lyrics_author = ""
    @property#Метод является свойством и возвращает информацию о текст песни
    def lyrics(self):
        return self._lyrics
    @lyrics.setter#Метод является сеттером для установки текста песни
    def lyrics(self, value):
        self._lyrics = value
    @property#Метод является свойством и возвращает информацию об авторе текста песни
    def lyrics_author(self):
        return self._lyrics_author
    @lyrics_author.setter#Метод является сеттером для установки автора текста песни
    def lyrics_author(self, value):
        self._lyrics_author = value
    def generate_description(self):#Создание условия песни
        try:
            if self.duration <= 0:
                raise ValueError("Продолжительность должна быть больше нуля.")
            return f"Песня: {self.name}\nТекст песни: {self.lyrics}\nАвтор текста песни: {self.lyrics_author}\nПродолжительность: {self.duration} секунды"
        except ValueError as e:
            print(f"Ошибка: {e}")
class InstrumentalComposition(MusicalComposition):#Класс наследуется от класса MusicalComposition и добавляет лдно дополнительных свойства
    def __init__(self):
        super().__init__()
        self._instruments = ""
    @property#Метод является свойством и возвращает информацию о инструментах
    def instruments(self):
        return self._instruments
    @instruments.setter#Метод является сеттером для установки инструментов
    def instruments(self, value):
        self._instruments = value
    def generate_description(self):#Создание условия песни
        try:
            if self.duration <= 0:
                raise ValueError("Продолжительность должна быть больше нуля")
            return f"Инструментальная композиция: {self.name}\nИнструменты: {self.instruments}\nПродолжительность: {self.duration} секунды"
        except ValueError as e:
            print(f"Error: {e}")
# Тестирование обработки исключений
collection = Collection()
collection.name = "Секретики"
collection.owner_name = "Райан Гослинг"
song = Song()
song.name = "Скибиди-туалет"
song.lyrics = "Вопрос сами придумайте"
song.lyrics_author = "Райан Гослинг"
song.duration = -10  # Вызов ошибки
instrumental_composition = InstrumentalComposition()
instrumental_composition.name = "Круто..."
instrumental_composition.instruments = "Укулеле"
instrumental_composition.duration = 300
#Вывод информации
print(collection.name)
print(collection.owner_name)
print(song.generate_description())  # Output error message due to invalid duration
print(instrumental_composition.generate_description())