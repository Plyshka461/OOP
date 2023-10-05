def poisk_pozicii(predlozh, k):#вводим функцию поиска позиции
    slova = predlozh.split() #Разделить строку на список слов
    pos = 0#Присваиваем значению расположения 0
    for word in slova:#Проводим итерацию для значения word в slova
        pos += len(word) + 1 #Учитываем длину слова и пробел после него
        if pos > k:#Если значение pos больше значения k
            return slova.index(word) + 1 #Возвращяем порядковый номер слова
    return len(slova) #Если k выходит за границы строки возвращаем номер последнего слова
predlozh = input('Введите тескт')#присваиваем значению текст
k = 69#присваиваем значению k переменную
word_number = poisk_pozicii(predlozh, k)#присваиваем значению word_number значение poisk_pozicii
print('Порядковый номер слова, накрывающего ',k,' позицию: ', word_number)#выводим результат