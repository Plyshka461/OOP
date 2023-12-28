from tkinter import *
from tkinter import ttk
window = Tk()#Создаем главное окно приложения
window.geometry("300x80")#Устанавливаем размер главного окна
value_var = IntVar()#Создаем переменную
pb = ttk.Progressbar(window, orient="horizontal", length = 280, variable=value_var, mode = 'determinate')#Создаем виджет прогрессбара
pb.pack()#Упаковываем виджет прогрессбара для отображения на экране
def start(): pb.start(100)#Создаем функцию которая запускает анимацию прогрессбара
def stop(): pb.stop()# Создаем функцию которая останавливает анимацию прогрессбара
start_btn = ttk.Button(text="Start", command=start)#Создаем кнопку с надписью Start, при нажатии на которую будет вызываться функция start
start_btn.pack()
stop_btn = ttk.Button(text="Stop", command=stop)#Создаем кнопку с надписью Stop, при нажатии на которую будет вызываться функция stop
stop_btn.pack()
window.mainloop()#Запускаем главный цикл обработки событий
