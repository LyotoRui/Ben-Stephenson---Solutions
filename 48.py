#Напишите программу, запрашивающую у пользователя дату его рожде-
#ния и выводящую на экран соответствующий знак зодиака.

month = input('Enter your birth month: ').lower()
day = int(input('Enter your day of the birth: '))

if month == 'december' and 22 <= day <= 31 or month == 'january' and 1 <= day <= 19:
    print('Your zodiac sign is Capricon')
elif month == 'january' and  20 <= day <= 31 or month == 'february' and 1 <= day <= 18:
    print('Your zodiac sign is Aquarius ')
elif month == 'february' and  19 <= day <= 29 or month == 'march' and 1 <= day <= 20:
    print('Your zodiac sign is Pisces')
elif month == 'march' and  21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
    print('Your zodiac sign is Aries')
elif month == 'april' and  20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
    print('Your zodiac sign is Taurus')
elif month == 'may' and  21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
    print('Your zodiac sign is Gemini')
elif month == 'june' and  21 <= day <= 30 or month == 'july' and  1 <= day <= 22 :
    print('Your zodiac sign is Cancer')
elif month == 'july' and  23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
    print('Your zodiac sign is Leo')
elif month == 'august' and  23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
    print('Your zodiac sign is Virgo')
elif month == 'september' and  23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
    print('Your zodiac sign is Libra')
elif month == 'october' and  23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
    print('Your zodiac sign is Scorpio')
elif month == 'november' and  22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
    print('Your zodiac sign is  Sagittarius')
