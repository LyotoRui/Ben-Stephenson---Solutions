#Напишите программу для измерения количества газа в молях при за-
#данных пользователем давлении, объеме и температуре. Проверьте свою 
#программу путем вычисления количества газа в  баллоне для дайвинга. 
#Типичный баллон вмещает 12 л газа под давлением 20 000 000 Па (при-
#мерно 3000 фунтов на кв. дюйм). Температуру в комнате примем за 20° 
#по шкале Цельсия или 68° по Фаренгейту.

R = 8.134
Kelvin = 273.15

pressure = float(input('Enter the pressure, Pa: '))	
volume = float(input('Enter the volume, L: '))	
temperature = float(input('Enter the temperature, C: '))	

temperature_to_kelvin = temperature + Kelvin
moles = int(pressure * volume / temperature * R)

print(f'The amount of moles in the gas is {moles}')