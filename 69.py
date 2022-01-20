#Напишите программу, которая будет запрашивать возраст всех посети-
#телей в группе (по одному за раз) и выводить общую цену билетов для по-
#сещения зоопарка этой группой. В качестве индикатора окончания ввода 
#можно по традиции использовать пустую строку. Общую цену билетов 
#стоит выводить в формате с двумя знаками после запятой.

visitor_list = []

visitor = input('Enter visitor`s age: ')

while True:
    visitor = input('Enter visitor`s age: ')
    if visitor == '':
        break
    visitor_list.append(int(visitor))

total_sum = 0

for age in visitor_list:
    if age < 2:
        pass
    elif age in range(3, 13):
        total_sum += 14
    elif age in range(13, 65):
        total_sum += 23
    else:
        total_sum += 18

print(f'Total cost: {total_sum}')
