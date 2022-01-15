money = int(input('Enter deposit`s amount: '))
for year in range(1, 4):
    money *= 1.04
    print(f'In {year} year deposit will be: ${money.__round__(2)}')