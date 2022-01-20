#Напишите программу, в которой пользователь сможет вводить значе-
#ния для переменных b и h, после чего на экране будет отображена площадь 
#треугольника с заявленными основанием и высотой.

floor = int(input('Enter triangle`s floor: '))
height = int(input('Enter triangle`s height: '))

print(f'Triangle`s area: {((floor * height) / 2).__round__(2)}')
