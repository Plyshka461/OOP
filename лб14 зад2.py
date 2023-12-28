from tkinter import *
window = Tk()#Создаем главное окно приложения
window.geometry("250x200")# Устанавливаем размер главного окна
#Создаем виджет Listbox
list1 = Listbox(window, height = 5, width = 15, selectmode = EXTENDED)
list2 = Listbox(window, height = 5, width = 15, selectmode = SINGLE)
#Создаем список
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин']
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']
#цикл который перебирает элементы списка и вставляем текущий элемент i в конец виджета
for i in lst1:
    list1.insert(END, i)
for i in lst2:
    list2.insert(END, i)
list1.pack()
list2.pack()
window.mainloop()
