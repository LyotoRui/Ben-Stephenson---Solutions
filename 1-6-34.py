count = int(input('Enter count of bread: '))
price = 3.49
discount_price = (3.49 * 0.6).__round__(2)

print(
    f'Normal price: {price}',
    f'60% off price: {discount_price}',
    f'Amount of bread: {count}',
    '----------',
    f'Total price: {(count * discount_price).__round__(2)}',
    sep='\n'
)