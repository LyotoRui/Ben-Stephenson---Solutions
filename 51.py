#Напишите программу, вычисляющую действительные корни квадра-
#тичной функции. Сначала вы должны запросить у пользователя значения 
#a, b и c. После этого должно быть выведено на экран количество действи-
#тельных корней функции и их значения.

from math import sqrt

a = float(input('Enter the coefficent of a: '))
b = float(input('Enter the coefficent of b: '))
c = float(input('Enter the coefficent of c: '))

if 2*a >= 0:
    root1 = (-b + sqrt(b ** 2 - 4*a*c)) / 2*a
    root2 = (-b - sqrt(b ** 2 - 4*a*c)) / 2*a
    print(root1, root2)
else:
    print('Equation has no real roots.')