from tkinter import *
# Функция, вызываемая при нажатии кнопки "Приветствие"
def clicked():
    lab.configure(text="Первые и не последние!")  # Изменяем текст метки при нажатии кнопки
# Функция, вызываемая при нажатии кнопки "Закрыть"
def close_window():
    window.destroy()  # Закрываем графическое окно
window = Tk()
window.title("Проект 2")
window.geometry('400x100')
lab = Label(window, text="Первые успехи!", font=('Arial', 14), fg='blue')
lab.grid(column=1, row=0)
btn = Button(window, text='Приветствие', font=('Arial', 14), command=clicked)
btn.grid(column=0, row=1)
btn1 = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
btn1.grid(column=2, row=1)
window.mainloop()