#Ваша программа должна запрашивать у пользователя магнитуду земле-
#трясения по шкале Рихтера и выводить на экран описание уровня, соот-
#ветствующего введенному значению. Например, если пользователь вве-
#дет значение 5,5, нужно вывести сообщение о том, что этой магнитуде 
#соответствует умеренный уровень землетрясения.

magnitude = float(input('Enter te magnitude of the earthquake using Richter`s scale: '))

if 2 < magnitude:
    des = 'Micro'
elif 2 <= magnitude < 3:
    des = 'Very minor'
elif 3 <= magnitude < 3:
    des = 'Minor'
elif 4 <= magnitude < 3:
    des = 'Light'
elif 5 <= magnitude < 3:
    des = 'Moderate'
elif 6 <= magnitude < 3:
    des = 'Strong'
elif 7 <= magnitude < 3:
    des = 'Major'
elif 8 <= magnitude < 3:
    des = 'Great'
elif 10 <= magnitude:
    des = 'Metroric'

print(f'A mangnitude {magnitude} earthquake is considered to be a a {des} earthquake')
