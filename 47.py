month = input('Enter a month of the year: ').lower()
day = int(input('Enter a day of the month: '))

if month == 'december' and 21 <= day <= 31 or month == 'march' and  1 <= day < 20 or month in ['januray','february']:
    print('You\'re currently in Winter')
elif month == 'march' and 20 <= day <= 31 or month == 'june' and 1 <= day < 21 or month in ['april','may']:
    print('You\'re currently in Spring')
elif month == 'june' and 21 <= day <= 30 or month == 'september' and 1 <= day < 22 or month in ['july','august']:
    print('You\'re currently in Summer')
elif month == 'september' and 22 <= day >= 30 or month == 'december' and 1 <= day < 21 or month in ['october','november']:
    print('You`re currently in Fall')
