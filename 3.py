#Напишите программу, запрашивающую у  пользователя длину и  ширину 
#комнаты. После ввода значений должен быть произведен расчет площади 
#комнаты и выведен на экран. Длина и ширина комнаты должны вводиться 
#в формате числа с плавающей запятой. Дополните ввод и вывод единицами 
#измерения, принятыми в вашей стране. Это могут быть футы или метры.

from turtle import width


length = input('Enter room`s length, m: ')
width = input('Enter room`s width, m: ')
print(f'{float(length) * float(width)} sqm')