year = int(input('Enter the year you intrested in: '))

if year % 400 == 0 or year % 4 == 0:
    print('This year is leap.')
else:
    print('This year is NOT leap.')