#Напишите программу, реализующую метод Ньютона для нахождения 
#квадратного корня числа x, введенного пользователем. Алгоритм реали-
#зации метода Ньютона следующий:
#-Запрашиваем число x у пользователя
#-Присваиваем переменной guess значение x / 2
#-Пока значение переменной guess не будет обладать должной точностью
#-Присваиваем переменной guess результат вычисления среднего между guess и x / guess

num = float(input('Enter number to find sqaure root: '))

initial = num / 2

while abs(initial * initial - num) >= 10e-20:
    initial = (initial + num / initial) / 2
    print('The square root of {} is {}'. format(num, initial))
