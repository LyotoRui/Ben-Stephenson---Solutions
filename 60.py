#Следующая формула может быть использована для определения дня не-
#дели, соответствующего 1 января заданного года:
#day_of_the_week = (year + floor((year - 1)/4) - floor((year - 1)/100) 
#+ floor((year - 1)/400))%7.
#В результате мы получим целое число, представляющее день недели от 
#воскресенья (0) до субботы (6).
#Используйте эту формулу для написания программы, запрашивающей 
#у пользователя год и выводящей на экран день недели, на который в за-
#данном году приходится 1 января. При этом на экран вы должны вывести 
#не числовой эквивалент дня недели, а его полное название.

from math import floor

pattern = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

year = int(input('Enter the year you intrested in: '))

day = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7

print(f'1st January wil be on {pattern[day]}')
