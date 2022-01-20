#Ваша функция должна обрабатывать числа в диапазоне 
#от 1 до 12. Если входящее значение выходит за границы этого диапазона, 
#вывод должен оставаться пустым. В основной программе запустите цикл 
#по натуральным числам от 1 до 12 и выведите на экран соответствующие 
#им числительные.

pattern = {
    1: 'First',
    2: 'Second',
    3: 'Third',
    4: 'Fourth',
    5: 'Fifth',
    6: 'Sixth',
    7: 'Seventh',
    8: 'Eighth',
    9: 'Ninth',
    10: 'Tenth',
    11: 'Eleventh',
    12: 'Twelfth'
}

def to_numeral(num : int):
    return pattern[num]

num = int(input('Enter num from 1 to 12: '))
if num in range(1, 13):
    print(f'Numeral is: {to_numeral(num)}')
else:
    print('Item is out of range.')