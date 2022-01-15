from math import pi, tan

lenght = int(input('Enter side`s lenght: '))
count = int(input('Enter sides amount: '))

area = (count * (lenght ** 2)) / (4 * tan(pi / count))

print(f'Area: {area}')