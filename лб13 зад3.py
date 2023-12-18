from tkinter import *
import random
# Функция для закрытия окна
def close_window():
    window.destroy()
# Функция для кубика
def roll_dice():
    # Генерируем случайное число от 1 до 6
    dice_number = random.randint(1, 6)
    # Заменяем текст метки на сгенерированное число
    lab.config(text=str(dice_number))
window = Tk()
window.title("Проект 3")
window.geometry('400x100')
lab = Label(window, text="Брось кубик", font=('Arial', 14))
lab.pack()
btn = Button(window, text='Бросить кубик', font=('Arial', 14), command=roll_dice)
btn.pack()
window.protocol("WM_DELETE_WINDOW", close_window)  # Обработчик закрытия окна
window.mainloop()