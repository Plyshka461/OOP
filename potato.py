class Potato:
    def __init__(self, number):
        self.number = number
        self.stage = 0
#Возвращает текущую стадию зрелости картошки
    def get_stage(self):
        stages = ["Саженец", "Проросток", "Зеленая", "Спелая"]
        return stages[self.stage]
#Увеличивает стадию зрелости картошки
    def grow(self):
        if self.stage < 3:
            self.stage += 1
#Вывод результата
potato1 = Potato(1)
print(f"Картошка {potato1.number}, стадия зрелости: {potato1.get_stage()}")  # Картошка 1, стадия зрелости: Саженец
potato1.grow()
print(f"Картошка {potato1.number}, стадия зрелости: {potato1.get_stage()}")  # Картошка 1, стадия зрелости: Проросток