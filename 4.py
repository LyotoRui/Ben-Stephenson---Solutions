from operator import length_hint
from turtle import width


width = input('Enter homestead`s width, ft: ')
length = input('Enter homestead`s length, ft: ')
print(f'{(float(width) * float(length)) / 43560} acre')