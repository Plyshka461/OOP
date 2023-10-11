list = [7, 1, 6, 9, 18, 99, 55]#создаем список
def menh_element(lst):#определяем функцию menh_element
    smallest_odd = None#присваиваем значению smallest_odd ничего
    for num in lst:#проводим итерацию num в lst
        if num % 2 != 0:#проверяем, является ли число нечетным
            if smallest_odd is None or num < smallest_odd:#если smallest_odd не пожходит или num меньше чем smallest_odd
                smallest_odd = num#то smallest_odd ровняется num
    return smallest_odd#возвращяемя к smallest_odd
result = menh_element(list)#присваиваем значению result значение menh_element
print(result)#выврдим результат