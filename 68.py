#В задаче 52 мы уже создавали таблицу соответствий между оценками 
#в буквенном и числовом выражении. Сейчас вам нужно будет рассчитать 
#среднюю оценку по произвольному количеству введенных пользователем 
#буквенных оценок. Для окончания ввода можно использовать индикатор 
#в виде пустой строки. Например, если пользователь последовательно вве-
#дет оценки A, затем C+, а после этого B и пустую строку, средний результат 
#должен составить 3,1.
#Для расчетов вам может пригодиться математика из упражнения 52. 
#Никаких проверок на ошибки проводить не нужно. Предположим, что 
#пользователь может вводить только корректные оценки или ноль.

grade = input('Enter your grade (press enter to quit): ').upper()

cgp = []

while grade != "":   
    if grade == 'A+' or grade == 'A':
        gp = 4.0
    elif grade == 'A-':
        gp = 3.7
    elif grade =='B+':
        gp = 3.3
    elif grade == 'B':
        gp = 3.0
    elif grade == 'B-':
        gp = 2.7
    elif grade == 'C+':
        gp = 2.3
    elif grade == 'C':
        gp = 2.0
    elif grade == 'C-':
        gp = 1.7
    elif grade == 'D+':
        gp = 1.3
    elif grade == 'D':
        gp = 1.0
    elif grade == 'F':
        gp = 0 
    else:
        gp = 'null'

    cgp.append(gp)
    grade = input('Enter your grade (press enter to quit): ').upper()   

cgpa = sum(cgp) / len(cgp)
print('Your CGPA is {}'. format(cgpa))
