temp = int(input('Enter temperature, C: '))

print(
    f'Temperature, F: {temp * 1.8 + 32}',
    f'Temperature, K: {temp + 273.15}',
    sep='\n'
)