pattern = {
    '1 January': 'New Year',
    '1 July': 'Canada`s Day',
    '25 December': 'Cristmas'
}

date = input('Enter day in format "Day Month": ')

if date in pattern.keys():
    print(f'It`s a {pattern[date]}')
else:
    print('There is no any holyday.')