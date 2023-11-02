#определяет объекты, представляющие города
class City:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
#определяет объекты, представляющие страны
class Country:
    def __init__(self, name, cities):
        self.name = name
        self.cities = cities
    @property
#возвращает количество городов в стране.
    def city_count(self):
        return len(self.cities)
#сортирует города по населению в порядке возрастания
    def sort_cities_by_population(self):
        self.cities.sort(key=lambda city: city.population)
#принимает минимальное и максимальное значения площади и возвращает список городов
    def find_cities_by_area(self, min_area, max_area):
        return [city for city in self.cities if min_area <= city.area <= max_area]
# Создание объектов класса City
city1 = City("Минск", 5000000, 25000)
city2 = City("Ошмяны", 69, 1000000000)
city3 = City("Новошишки", 1, 100)
city4 = City("Островец", 99, 1000)
# Создание объекта класса Country
country = Country("Беларусь", [city1, city2, city3, city4])
# Вывод количества городов в стране
print("Количество городов в стране:", country.city_count)
# Сортировка городов по количеству жителей
country.sort_cities_by_population()
print("\nСортировка городов по количеству жителей:")
for city in country.cities:
    print(f"Город: {city.name}, Население: {city.population} человек")
# Поиск городов в заданном диапазоне площади
min_area = 100
max_area = 1000000000000000
filtered_cities = country.find_cities_by_area(min_area, max_area)
print("\nГорода, соответствующие заданному диапазону площади:")
for city in filtered_cities:
    print(f"Город: {city.name}, Площадь: {city.area} км²")