#В данном задании вам предстоит написать программу, которая будет пе-
#реводить введенное пользователем значение давления в  килопаскалях 
#(кПа) в фунты на квадратный дюйм (PSI), миллиметры ртутного столба 
#и  атмосферы. Коэффициенты и  формулы для перевода найдите само-
#стоятельно.

pressure = int(input('Enter pressure, kPa: '))

print(
    f'PSI: {pressure * 0.1450377377302}'
)