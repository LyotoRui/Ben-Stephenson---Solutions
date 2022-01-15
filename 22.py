from math import sqrt

s1 = int(input('Enter the first side: '))
s2 = int(input('Enter the second side: '))
s3 = int(input('Enter the third side: '))
s = (s1 + s2 + s3) / 2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print(f'The triangle`s area: {area}')