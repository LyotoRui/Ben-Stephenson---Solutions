pattern = {
    '1 January': 'New Year',
    '1 July': 'Canada`s Day',
    '25 December': 'Cristmas'
}

date = input('Enter day in format "Day Month": ')

#Напишите программу, которая будет запрашивать у пользователя день 
#и  месяц. Если введенные данные в точности указывают на один из пе-
#речисленных в таблице праздников, необходимо вывести его название. 
#В противном случае сообщить, что на заданную дату праздники не при-
#ходятся.

if date in pattern.keys():
    print(f'It`s a {pattern[date]}')
else:
    print('There is no any holyday.')
