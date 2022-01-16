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