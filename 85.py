#Напишите функцию, принимающую на вход длины двух катетов прямо-
#угольного треугольника и возвращающую длину гипотенузы, рассчитан-
#ную по теореме Пифагора. В главной программе должен осуществляться 
#запрос длин сторон у  пользователя, вызов функции и  вывод на экран 
#полученного результата.

from math import sqrt

def hypotenuse(cat_1 : int, cat_2 : int):
    return sqrt((cat_1 ** 2) + (cat_2 ** 2))

cat_1 = int(input('Enter first cathetus: '))
cat_2 = int(input('Enter secont cathetus: '))

print(hypotenuse(cat_1, cat_2))
