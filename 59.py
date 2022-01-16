#Разработайте программу, принимающую на вход дату и  выводящую на 
#экран дату, следующую за ней. Например, если пользователь введет дату, 
#соответствующую 18 ноября 2019 года, на экран должен быть выведен 
#следующий день, то есть 19 ноября 2019 года. Если входная дата будет 
#представлять 30 ноября, то на выходе мы должны получить 1 декабря. 
#И наконец, если ввести последний день года – 31 декабря 2019-го, пользо-
#ватель должен увидеть на экране дату 1 января 2020-го. Дату пользователь 
#должен вводить в три этапа: год, месяц и день. Убедитесь, что ваша про-
#грамма корректно обрабатывает високосные годы.

date = input('Enter a date in the format (Year-Month-Day): ' )

date = date.split('-')
year, month, day = int(date[0]), int(date[1]), int(date[2])
days_30  = [9,4,6,11]
days_31 = [1,3,5,7,8,10]

if year % 400 == 0 or year % 4 == 0:
    leap = True
    feb = 29 
elif year % 100 == 0:
    leap = False
    feb = 28
else:
    leap = False


if month == 2 and leap:
    if 1 <= day <= 28:
        day += 1
        month = month 
        year = year 
    elif day == 29:
        day = 1
        month += 1
        year = year 
elif month == 2 and not leap:
    if 1 <= day < 28:
        day += 1
        month = month 
        year = year
    elif day == 28:
        day = 1
        month += 1
        year = year 
elif month == 12:
    if 1 <= day < 31:
        day += 1
        month = month
        year = year 
    elif day == 31:
        day = 1
        month = 1
        year += 1 
elif month in days_30:
    if 1 <= day < 30:
        day += 1 
        month = month 
        year = year
    elif day == 30:
        day = 1
        month += 1
        year = year 
elif month in days_31:
    if 1 <= day < 31:
        day += 1 
        month = month 
        year = year 
    elif day == 31:
        day = 1
        month += 1
        year = year 

print('{}-{:0>2d}-{:0>2d}'. format(year, month, day))