class Counter:
    def init(self, start_value=0):
        self.value = start_value
# Конструктор класса Counter создает объект Counter и инициализирует его значение start_value
    def start_from(self, start_value=0):
        self.value = start_value
# Метод start_from устанавливает значение счетчика равным start_value
    def increment(self):
        self.value += 1
# Метод increment увеличивает значение счетчика на 1
    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

# Метод display выводит текущее значение счетчика на экран
    def reset(self):
        self.value = 0
counter = Counter()#Создаем экземпляр счетчика с начальным значением 0
counter.display()#Выводит "Текущее значение счетчика = 0"
counter.increment()#Увеличиваем счетчик на 1
counter.display()#Выводит "Текущее значение счетчика = 1"
counter.start_from(10)#Устанавливаем начальное значение 10
counter.display()#Выводит "Текущее значение счетчика = 10"
counter.reset()#Обнуляем счетчик
counter.display()#Выводит "Текущее значение счетчика = 0"