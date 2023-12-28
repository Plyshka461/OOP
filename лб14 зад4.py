from tkinter import *
from tkinter import ttk
import math
def tabulate():
    # Очистка списка перед новым табулированием
    listbox.delete(0, END)
    # Значения параметра для табулирования
    start = 0.01
    end = 0.9
    step = 0.01
    # Общее количество шагов
    total_steps = int((end - start) / step) + 1
    # Установка значений для прогрессбара
    pb.config(maximum=total_steps, value=0)
    for i in range(total_steps):
        # Вычисление значения функции
        x = start + i * step
        y = 1 + math.log(2 * x)
        # Добавление значения в список
        listbox.insert(END, f"x = {format(x, '.2f')}, y = {format(y, '.4f')}")
        # Увеличение значения прогрессбара
        pb.step()
def start():
    # Блокируем кнопку "Start" и запускаем табулирование
    start_btn.config(state=DISABLED)
    tabulate()
def stop():
    # Останавливаем табулирование и разблокируем кнопку "Start"
    start_btn.config(state=NORMAL)
window = Tk()
window.geometry("400x300")
# Создание виджета прогрессбара
pb = ttk.Progressbar(window, orient="horizontal", length=380, mode='determinate')
# Создание виджета списка
listbox = Listbox(window, width=50)
# Создание кнопок "Start" и "Stop"
start_btn = ttk.Button(window, text="Start", command=start)
stop_btn = ttk.Button(window, text="Stop", command=stop)
# Размещение виджетов на форме
pb.pack(pady=10)
listbox.pack()
start_btn.pack(pady=10)
stop_btn.pack()
window.mainloop()