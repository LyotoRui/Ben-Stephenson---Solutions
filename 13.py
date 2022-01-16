#Напишите программу, которая будет запрашивать у пользователя сум-
#му сдачи в центах. После этого она должна рассчитать и вывести на экран, 
#сколько и каких монет потребуется для выдачи указанной суммы, при ус-
#ловии что должно быть задействовано минимально возможное количество монет. Допустим, у нас есть в распоряжении монеты достоинством в 1, 
#5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.

toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5

cost = float(input('Enter total cost, $: '))
cents = cost * 100

print(' ', cents // toonie, 'toonies')
cents = cents % toonie

print(' ', cents // loonie, 'loonies')
cents = cents % loonie

print(' ', cents // quarter, 'quarter')
cents = cents % quarter

print(' ', cents // dime, 'dime')
cents = cents % dime

print(' ', cents // nickel, 'nickel')
cents = cents % nickel	

print('', cents, 'pennies')