#Разработайте программу, запрашивающую у  пользователя целое четы-
#рехзначное число и подсчитывающую сумму составляющих его цифр. На-
#пример, если пользователь введет число 3141, программа должна вывести 
#следующий результат: 3 + 1 + 4 + 1 = 9.

num = str(input('Enter the number: '))
sum = 0

for i in num:
    sum += int(i)

print(f'The sum is: {sum}')
