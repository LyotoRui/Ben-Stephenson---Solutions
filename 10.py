#Создайте программу, которая запрашивает у пользователя два целых чис-
#ла a и b, после чего выводит на экран результаты следующих математи-
#ческих операций:
# сумма a и b; 
# разница между a и b; 
# произведение a и b; 
# частное от деления a на b; 
# остаток от деления a на b; 
# десятичный логарифм числа a; 
# результат возведения числа a в степень b.

from math import log10

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(
    a + b,
    a - b,
    a * b,
    a / b,
    a % b,
    log10(a),
    a ** b,
    sep='\n'
    )
