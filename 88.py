#Напишите функцию, которая будет принимать на вход три числа в качестве параметров и возвращать их медиану. В основной программе должен 
#производиться запрос к пользователю на предмет ввода трех чисел, а так-
#же вызов функции и отображение результата.

def median(*items):
    return sorted(items)[1]

a = int(input('Enter first num: '))
b = int(input('Enter second num: '))
c = int(input('Enter third num: '))

print(f'Median is {median(a, b, c)}')
