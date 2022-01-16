#Напишите программу, которая будет принимать на вход буквенную 
#оценку и выводить на экран соответствующую оценку в числовом выра-
#жении. Убедитесь в том, что программа генерирует понятное сообщение 
#об ошибке при неверном вводе.

pattern = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0
}

grade = input('Enter grade: ').upper()

print(f'Points: {pattern[grade]}')
