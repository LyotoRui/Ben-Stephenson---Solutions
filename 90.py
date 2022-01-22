#Напишите программу, которая будет сама строить куплеты этой песен-
#ки. В программе должна присутствовать функция для отображения одного 
#куплета. В качестве входного параметра она должна принимать порядко-
#вый номер дня, а в качестве результата возвращать готовый куплет. Далее 
#в основной программе эта функция должна быть вызвана 12 раз подряд. 
#Каждая строка с  очередным подарком должна присутствовать в  вашей 
#программе лишь раз, за исключением строки «A partridge in a pear tree». 
#В этом случае вы можете отдельно хранить такой вид строки для первого 
#куплета и слегка измененный («And a partridge in a pear tree») – для всех 
#последующих.

def int_ordinal(num):
    if num <= 0 or num > 12:
        return ''
    else:
        if num == 1:
            return 'First'
        elif num == 2:
            return 'Second'
        elif num == 3:
            return 'Third'
        elif num == 4:
            return 'Fourth'
        elif num == 5:
            return 'Fifth'
        elif num == 6:
            return 'Sixth'
        elif num == 7:
            return 'Seventh'
        elif num == 8:
            return 'Eighth'
        elif num == 9:
            return 'Ninth'
        elif num == 10:
            return 'Tenth'
        elif num == 11:
            return 'Eleventh'
        elif num == 12:
            return 'Twelfth'

def verse(n):
    print('On the {} day of Christmas'. format(int_ordinal(n))) 
    print('my true love sent to me: ')
    
    if n >= 12:
        print('12 drummers drumming')
    elif n >= 11:
        print('11 pipers piping')
    elif n >= 10:
        print('10 lords a-leaping')
    elif n >= 9:
        print('Nine ladies dancing')
    elif n >= 8:
        print('Eight maids a-milking')
    elif n >= 7:
        print('Seven swans a-swimming')
    elif n >= 6:
        print('Six geese a-laying')
    elif n >= 5:
        print('Five golden rings')
    elif n >= 4:
        print('Four calling birds')
    elif n >= 3:
        print('Three french hens')
    elif n >= 2:
        print('Two turtle doves, and')
    elif n == 1:
        print('A partridge in a pear tree')

def main():
    for i in range(1,13):
        verse(i)

main()
