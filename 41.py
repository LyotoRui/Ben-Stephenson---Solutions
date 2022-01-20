#Напишите программу, которая будет запрашивать у пользователя дли-
#ны всех трех сторон треугольника и выдавать сообщение о том, к какому 
#типу следует его относить.

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

if a == b == c:
    print('Your triangle is equilateral.')
elif a == b != c or a == c != b or b == c != a:
    print('Your triangle is isofemoral.')
else:
    print('Your triangle is versatile.')
