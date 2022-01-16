pattern = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

cell = input('Enter the cell: ')

if sum([pattern[cell[0].lower()], int(cell[1])]) % 2 == 0:
    print('Your cell is Black.')
else:
    print('Your cell is White.')
