freq = input('Enter wave`s frequency: ')

if freq < 3 * (10 ** 9):
    print('Radio waves')
elif freq in range(3 * (10 ** 9), 3 * (10 ** 12)):
    print('Microwaves')
elif freq in range(3 * (10 ** 12), 4.3 * (10 ** 14)):
    print('Infrared radiation')
elif freq in range(4.3 * (10 ** 14), 7.5 * (10 ** 14)):
    print('Visible radiation')
elif freq in range(7.5 * (10 ** 14), 3 * (10 ** 17)):
    print('Ultraviolet radiation')
elif freq in range(3 * (10 ** 17), 3 * (10 ** 19)):
    print('X-ray radiation')
else:
    print('Gamma radiation')