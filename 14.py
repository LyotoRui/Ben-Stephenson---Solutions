#Многие люди на планете привыкли рассчитывать рост человека в футах 
#и дюймах, даже если в их стране принята метрическая система. Напишите 
#программу, которая будет запрашивать у пользователя количество футов, 
#а  затем дюймов в  его росте. После этого она должна пересчитать рост 
#в сантиметры и вывести его на экран.

foot = int(input('Enter feet, ft: '))
inch = int(input('Enter inches, inch: '))

print(f'Your tall: {((foot * 12 + inch) * 2.54).__round__(2)}')
