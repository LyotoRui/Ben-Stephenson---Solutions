#Это упражнение преследует цель идентификации количества смен макси-
#мального значения в коллекции случайных чисел. Ряд должен быть запол-
#нен числами от 1 до 100. При этом последовательность может содержать 
#дубликаты, а некоторых чисел из диапазона от 1 до 100 в ней может не 
#быть.

from random import randrange

num = 100
max_num = randrange(1, num + 1)
print(max_num)

updates = 0

for i in range(1, num):
    current = randrange(1, num + 1)
    if current > max_num:
        max_num = current
        updates += 1
        print('{}   <= Update'. format(current))
    else:
        print(current)

print('The maximum number found was', max_num)
print(f'The maximum number was updated {updates} times')
