#Напишите программу для расчета индекса массы тела (body mass index – 
#BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
#используете одну из приведенных ниже формул для определения индекса.

weight = int(input('Enter your weight: '))
height = int(input('Enter your height: '))

print(f'Your BMI is {(weight / (height ** 2))}')