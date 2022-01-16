#Запросите у пользователя длину волны и выведите на экран соответ-
#ствующий ей цвет. Если введенное пользователем значение длины волны 
#окажется за пределами видимой части спектра, сообщите об этом.

wavelength = float(input('Enter the wavelength of your color in nanometeres(nm): '))

if wavelength in range(380, 450):
    print('Spectre color is Purple.')
elif wavelength in range(450, 495):
    print('Spectre color is Blue.')
elif wavelength in range(495, 570):
    print('Spectre color is Green.')
elif wavelength in range(570, 590):
    print('Spectre color is Yellow.')
elif wavelength in range(590, 620):
    print('Spectre color is Orange.')
elif wavelength in range(620, 751):
    print('Spectre color is Red.')
else:
    print('Spectre color is invisible.')