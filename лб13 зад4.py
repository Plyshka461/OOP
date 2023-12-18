import tkinter as tk
import math
# Функция для калькулятора и математического вычисления
def calculate():
    x = float(entry.get())
    result = (1/7 + math.log(math.sqrt(x))) * math.exp(math.sqrt(x-2))
    result_label.configure(text=f"Результат: {result}")
# Создание графического интерфейса
window = tk.Tk()
window.title("Подсчет по формуле")
window.geometry("300x200")
# Ввод значения x
label = tk.Label(window, text="Введите значение x:")
label.place(x=50, y=30)
entry = tk.Entry(window)
entry.place(x=50, y=50)
# Кнопка для подсчета
button = tk.Button(window, text="Посчитать", command=calculate)
button.place(x=50, y=80)
# Поле для вывода результата
result_label = tk.Label(window, text="")
result_label.place(x=50, y=110)
# Запуск главного цикла программы
window.mainloop()