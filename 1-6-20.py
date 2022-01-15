R = 8.134
Kelvin = 273.15

pressure = float(input('Enter the pressure, Pa: '))	
volume = float(input('Enter the volume, L: '))	
temperature = float(input('Enter the temperature, C: '))	

temperature_to_kelvin = temperature + Kelvin
moles = int(pressure * volume / temperature * R)

print(f'The amount of moles in the gas is {moles}')