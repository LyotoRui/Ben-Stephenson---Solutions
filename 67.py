#Напишите программу для расчета периметра заданного многоугольника. 
#Начните с запроса у пользователя координат x и y первой точки много-
#угольника. Продолжайте запрашивать координаты следующих точек фи-
#гуры, пока пользователь не оставит строку ввода координаты по оси x
#пустой. После ввода каждой пары значений вы должны вычислить длину 
#очередной стороны многоугольника и  прибавить полученное значение 
#к будущему ответу. По окончании ввода необходимо вычислить расстояние от последней введенной точки до первой, чтобы замкнуть фигуру, 
#и  вывести итоговый результат.

from math import sqrt

perimeter = 0 

originx = float(input('Enter the X cordinate: '))
originy = float(input('Enter the Y cordinate: '))

lastx = originx
lasty = originy

current = float(input('Enter the X cordinate (Press enter to end): '))
while current != '':
    currentx = float(current)
    currenty = float(input('Enter the Y cordinate: '))
    distance = sqrt((lastx - currentx) **2  + (lasty - currenty ) ** 2)
    perimeter += distance

    lastx = currentx
    lasty = currenty

    current = input('Enter the X cordinate (Press enter to end): ')
    
distance = sqrt((originx - currentx) ** 2 + (originy - currenty) ** 2)
perimeter += distance

print('The perimeter of the polygon is {}'. format(perimeter))