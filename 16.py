from math import pi

r = int(input('Enter the radius: '))
print(
    (pi * r ** 2).__round__(2),
    ((4 * pi * r ** 3) / 3).__round__(2),
    sep='\n'
)