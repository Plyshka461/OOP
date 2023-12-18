from tkinter import *
# Функция для закрытия окна
def close_window():
    window.destroy()
# Создание главного окна
window = Tk()
window.title("Проект 1")
window.geometry('400x100')
# Создание метки
lab = Label(window, text="Моя первая программа", font=('Arial', 14))
lab.pack()
# Создание кнопки
btn = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
btn.pack()
# Запуск главного цикла программы
window.mainloop()