#Напишите программу, которая будет запрашивать целое число у поль-
#зователя. Если пользователь введет значение, меньшее двух, необходимо 
#вывести соответствующее сообщение об ошибке. Иначе нужно перечис-
#лить в столбец список простых множителей заданного числа, которые при 
#перемножении дали бы исходное число.

factor = 2
n = int(input('Enter the num: '))
print(f'Simple of {n}:')

while factor <= n:
    if n % factor == 0:
        print(factor)
        n = int(n / factor)
    else:
        factor += 1
