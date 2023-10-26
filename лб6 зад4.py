from potato import Potato
#Создание класса грядка
class PotatoBed:
    def __init__(self, num_potatoes):
        self.potatoes = [Potato(i+1) for i in range(num_potatoes)]
#Увеличивает стадию зрелости всех картошек на грядке
    def grow_potatoes(self):
        for potato in self.potatoes:
            potato.grow()
#Возвращает список стадий зрелости всех картошек на грядке
    def get_potato_stages(self):
        stages = [potato.get_stage() for potato in self.potatoes]
        return stages
# Пример использования класса PotatoBed
potato_bed = PotatoBed(5)
print("Изначальные стадии зрелости картошек:", potato_bed.get_potato_stages())
potato_bed.grow_potatoes()
print("Стадии зрелости картошек после первого роста:", potato_bed.get_potato_stages())
potato_bed.grow_potatoes()
print("Стадии зрелости картошек после второго роста:", potato_bed.get_potato_stages())
potato_bed.grow_potatoes()
print("Стадии зрелости картошек после третьего роста:", potato_bed.get_potato_stages())