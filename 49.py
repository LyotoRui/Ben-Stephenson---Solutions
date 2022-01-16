year = int(input('What year is it? '))
if year >= 0:
    if year % 12 == 8:
        print('Year of the Dragon')
    elif year % 12 == 9: 
        print('Year of the  Snake')
    elif year % 12 == 10: 
        print('Year of the  Horse')
    elif year % 12 == 11: 
        print('Year of the  Sheep')
    elif year % 12 == 0: 
        print('Year of the  Monkey')
    elif year % 12 == 1: 
        print('Year of the  Rooster')
    elif year % 12 == 2: 
        print('Year of the  Dog')
    elif year % 12 == 3: 
        print('Year of the  Pig')
    elif year % 12 == 4: 
        print('Year of the Rat')
    elif year % 12 == 5: 
        print('Year of the  Ox')
    elif year % 12 == 6: 
        print('Year of the Tiger')
    elif year % 12 == 7: 
        print('Year of the Hare')
else:
    print ('Enter a valid year greater than or equals to 0')