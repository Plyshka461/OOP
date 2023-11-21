class Cars:
    def __init__(self, brand, year, price, configuration, country, date_of_sale, buyer_name):##инициализирует атрибуты объекта
        self.brand = brand
        self.year = year
        self.price = price
        self.configuration = configuration
        self.country = country
        self.date_of_sale = date_of_sale
        self.buyer_name = buyer_name
    def __str__(self):#возвращает строку, описывающую марку, год, цену, вид кузова,страна производства, дата продажи, имя покупателя
        return f"Brand: {self.brand}\nYear: {self.year}\nPrice: {self.price}\nConfiguration: {self.configuration}\nCountry: {self.country}\nDate of Sale: {self.date_of_sale}\nBuyer Name: {self.buyer_name}"
#класс подержаные авто
class UsedCars(Cars):#вызывает конструктор родительского класса Cars и инициализирует дополнительные атрибуты объекта
    def __init__(self, brand, year, price, configuration, country, date_of_sale, buyer_name, preservation_degree, owner_name, mileage):
        super().__init__(brand, year, price, configuration, country, date_of_sale, buyer_name)
        self.preservation_degree = preservation_degree
        self.owner_name = owner_name
        self.mileage = mileage
    def __str__(self):#возвращает строку, описывающую состояние, имя продавца, пробег
        return super().__str__() + f"\nPreservation Degree: {self.preservation_degree}\nOwner Name: {self.owner_name}\nMileage: {self.mileage}"
class SportsCars(Cars):#вызывает конструктор родительского класса Cars и инициализирует дополнительные атрибуты объекта
    def __init__(self, brand, year, price, configuration, country, date_of_sale, buyer_name, time_to_speed, engine_capacity, power):
        super().__init__(brand, year, price, configuration, country, date_of_sale, buyer_name)
        self.time_to_speed = time_to_speed
        self.engine_capacity = engine_capacity
        self.power = power
    def __str__(self):#возвращает строку, описывающую 0-100, объем двигателя, мощность
        return super().__str__() + f"\nTime to Speed: {self.time_to_speed} seconds\nEngine Capacity: {self.engine_capacity}\nPower: {self.power}"
class SpecialEquipment(Cars):#вызывает конструктор родительского класса Cars и инициализирует дополнительные атрибуты объекта
    def __init__(self, brand, year, price, configuration, country, date_of_sale, buyer_name, equipment_type, weight, dimensions):
        super().__init__(brand, year, price, configuration, country, date_of_sale, buyer_name)
        self.equipment_type = equipment_type
        self.weight = weight
        self.dimensions = dimensions
    def __str__(self):#возвращает строку, описывающую тип оборудования, вес, размер
        return super().__str__() + f"\nEquipment Type: {self.equipment_type}\nWeight: {self.weight}\nDimensions: {self.dimensions}"
#Пример использования
car1 = UsedCars("Lada", 1978, 300, "Sedan", "Russia", "2022-01-01", "John Doe", "Very bad", "Jane Smith", 500000)
print(car1)
car2 = SportsCars("Ferrari", 2022, 500000, "Coupe", "Italy", "2022-02-01", "Jane Smith", 3.5, "3.9L", 710)
print(car2)
car3 = SpecialEquipment("Caterpillar", 2015, 1000000, "Excavator", "USA", "2022-03-01", "John Doe", "Construction",50000, "10m x 4m x 3m")
print(car3)