foot = int(input('Enter feet, ft: '))
inch = int(input('Enter inches, inch: '))

print(f'Your tall: {((foot * 12 + inch) * 2.54).__round__(2)}')