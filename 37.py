letter = str(input('Enter any letter: '))

if letter in 'AaEeIiOoUu':
    print('Your letter is vovel.')
elif letter in 'Yy':
    print('Your letter can be vovel or constant.')
else:
    print('Your letter is constant.')