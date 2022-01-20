#Напишите программу, которая будет запрашивать у пользователя но-
#минал банкноты и отображать на экране имя деятеля, портрет которого 
#размещен на соответствующем денежном знаке. Если банкноты введен-
#ного номинала не существует, должно выводиться сообщение об ошибке.

pattern = {
    1: 'George Washington',
    2: 'Thomas Jefferson',
    5: 'Abraham Lincoln',
    10: 'Alexander Hamilton',
    20: 'Andrew Jackson',
    50: 'Ulysses Grant',
    100: 'Benjamin Franklin'
}

value = int(input('Enter dollar value: '))

if value in pattern.keys():
    print(f'{pattern[value]} is on ${value}.')
else:
    print('There is no such value.')
