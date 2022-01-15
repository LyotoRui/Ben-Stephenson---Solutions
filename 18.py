from math import pi

radius = float(input('Enter the radius: '))
height = float(input('Enter the height: '))

print(((pi * (radius ** 2)) * height).__round__(1))