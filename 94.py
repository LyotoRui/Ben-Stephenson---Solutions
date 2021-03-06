#Напишите функцию для определения возможности построения треугольника на 
#основании длин трех его потенциальных сторон. Функция 
#должна принимать три числовых параметра и возвращать булево значе-
#ние. Если длина хотя бы одной из трех сторон меньше или равна нулю, 
#функция должна вернуть False. В противном случае необходимо выпол-
#нить проверку на допустимость построения треугольника на основании 
#введенных длин сторон и вернуть соответствующее значение. Напиши-
#те основную программу, запрашивающую у пользователя длины сторон 
#и выводящую на экран информацию о том, может ли при заданных зна-
#чениях получиться треугольник.

def is_triangle(a: int, b: int, c: int):
    sides = sorted([a, b, c])
    return sides[-1] < sum(sides[:-1])
    

a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

print(is_triangle(a, b, c))