rating = float(input('What is your employee rating? '))

pay_raise = rating * 2400

if rating == 0.0:
    print('Your pay rose by: {}'. format(pay_raise))
elif rating == 0.4:
    print('Your pay rose by: {}'. format(pay_raise))
elif rating >= 0.6:
    print('Your pay rose by: {}'. format(pay_raise))
else:
    print('Enter a valid employee rating')