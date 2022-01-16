#Создайте программу, запрашивающую у  пользователя длину и  ширину 
#садового участка в футах. Выведите на экран площадь участка в акрах.

width = input('Enter homestead`s width, ft: ')
length = input('Enter homestead`s length, ft: ')
print(f'{(float(width) * float(length)) / 43560} acre')