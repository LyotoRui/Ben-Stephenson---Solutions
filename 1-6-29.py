temp = int(input('Enter temperature, C: '))
speed = int(input('Enter wind speed, m/s: '))

wci = 13.12 + (0.6215 * temp) - 11.37 * (speed ** 0.16) + 0.3965 * temp * (speed ** 0.16)

print(f'WCI is {wci}')