#Напишите программу, которая будет запрашивать у пользователя целое 
#число и  выводить все числа, начиная с  введенного числа и  заканчивая 
#единицей. После этого пользователь должен иметь возможность ввести 
#другое число и снова получить ряд чисел, называемый сиракузской по-
#следовательностью. Условием выхода из программы должен быть ввод 
#пользователем нуля или отрицательного числа.

num = int(input('Enter the number: '))
result = []

while num != 0:
    if num == 1:
        print(result)
        num = int(input('Enter the number: '))
        result.clear()
    elif num <= 0:
        print('Exit programm...')
        break
    elif num % 2 == 0:
        num = int(num // 2)
        result.append(num)
    elif num % 2 != 0:
        num = num * 3 + 1
        result.append(num)
    