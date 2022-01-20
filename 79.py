#Напишите программу, запрашивающую у  пользователя два положи-
#тельных целых числа и выводящую для них наибольший общий делитель.

m = int(input('Enter the first number: '))
n = int(input('Enter the second number: '))

d = min(m,n)

while m % d != 0 or n % d != 0:
    d -= 1
    print('{} is the common divisor of {} and {}'. format(d, m, n))
    