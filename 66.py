#Напишите программу, запрашивающую у пользователя цены, пока не 
#будет введена пустая строка. На первой строке выведите сумму всех вве-
#денных пользователем сумм, а  на второй – сумму, которую покупатель 
#должен заплатить наличными. Эта сумма должна быть округлена до бли-
#жайших пяти центов. Вычислить сумму для оплаты наличными можно, 
#получив остаток от деления общей суммы в  центах на 5. Если он будет 
#меньше 2,5, следует округлить сумму вниз, а если больше – вверх.

price = input('Enter the price(s) of items bought (enter a blank line to end): ')

pennies_per_nickel = 5
nickel = 0.05
total = 0
while price != '':
    total += float(price)
    price = input('Enter the price(s) of items bought (Press enter to end): ')

print('The total amount payable is {:.2f}'. format(total))

payable_using_nickels = total * 100 % pennies_per_nickel

if payable_using_nickels < pennies_per_nickel / 2:
    cash_payable = total - payable_using_nickels
else:
    cash_payable = total + nickel - payable_using_nickels

print('The amount payable with cash is {}'. format(cash_payable))