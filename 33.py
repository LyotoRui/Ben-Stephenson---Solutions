#Напишите программу, запрашивающую у пользователя три целых числа 
#и выводящую их в упорядоченном виде – по возрастанию. Используйте 
#функции min и max для нахождения наименьшего и наибольшего значений. 
#Оставшееся число можно найти путем вычитания из суммы трех введен-
#ных чисел максимального и минимального.

nums = [
    int(input('Enter first number: ')),
    int(input('Enter second number: ')),
    int(input('Enter third number: '))
]

for i, item in zip(range(1, 4), sorted(nums)):
    print(f'{i} - {item}')