#Напишите программу, определяющую вид фигуры по количеству ее сто-
#рон. Запросите у пользователя количество сторон и выведите сообщение 
#с  указанием вида фигуры. Программа должна корректно обрабатывать 
#и выводить названия для фигур с количеством сторон от трех до десяти 
#включительно. Если введенное пользователем значение находится за гра-
#ницами этого диапазона, уведомите его об этом.

side = int(input('How many sides does your shape have: '))

if side == 3:
    print('Triangle')
elif side == 4:
    print('Rectangle, Squre, Kite, Paralellogram or Trapezium')
elif side == 5:
    print('Pentagon')
elif side == 6:
    print('Hexagon')
elif side == 7:
    print('Heptagon')
elif side == 8:
    print('Octagon')
elif side == 9:
    print('Nonagon')
elif side == 10:
    print('Decagon')
else:
    print('Input is out of range')