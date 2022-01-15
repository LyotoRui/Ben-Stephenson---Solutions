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