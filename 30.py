#Напишите программу, которая будет запрашивать у пользователя значение 
#температуры в градусах Цельсия и отображать эквивалентный показатель 
#по шкалам Фаренгейта и Кельвина. Необходимые коэффициенты и фор-
#мулы для проведения расчетов нетрудно найти на просторах интернета.

temp = int(input('Enter temperature, C: '))

print(
    f'Temperature, F: {temp * 1.8 + 32}',
    f'Temperature, K: {temp + 273.15}',
    sep='\n'
)
