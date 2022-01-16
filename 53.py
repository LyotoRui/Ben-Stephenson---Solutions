#В предыдущем упражнении мы переводили буквенные оценки студен-
#тов в  числовые. Сейчас перевернем ситуацию и  попробуем определить 
#буквенный номинал оценки по его числовому эквиваленту. Убедитесь 
#в том, что ваша программа будет обрабатывать числовые значения между 
#указанными в табл. 2.13. В этом случае оценки должны быть округлены до 
#ближайшей буквы. Программа должна выдавать оценку A+, если введен-
#ное пользователем значение будет 4,0 и выше.

gp = round( float(input('Enter your grade point: ')), 2)

if gp == 4.0:
    grade = 'A+'
elif 3.7 <= gp < 4.0:
    grade = 'A-'
elif 3.3 <= gp < 3.7:
    grade = 'B+'
elif 3.0 <= gp < 3.3:
    grade = 'B'
elif 2.7 <= gp < 3.0:
    grade = 'B-'
elif 2.3 <= gp < 2.7:
    grade = 'C+'
elif 2.0 <= gp < 2.3:
    grade = 'C'
elif 1.7 <= gp < 2.0:
    grade = 'C-'
elif 1.3 <= gp < 1.7:
    grade = 'D+'
elif 1.0 <= gp < 1.3:
    grade = 'D'
elif 0 <= gp < 1.0:
    grade = 'F'
else:
    grade = 'null'

if grade == 'null':
    print('Please enter a valid grade point')
else:
    print('Grade = {}'. format(grade))