#Напишите программу, реализующую этот алгоритм. Пользователь дол-
#жен ввести год, для которого его интересует дата Пасхи, и получить ответ 
#на свой вопрос.

year = int(input('Enter the year: '))

a = int(year) % 19
b = int(int(year) // 100)
c = int(year) % 100
d = int(b // 4)
e = b % 4
f = int((b + 8) / 25)
g = int((b - f + 1) / 3)
h = (19 * a + b - d - g + 15) % 30
i = int(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = int((a + 11 * h + 22 * l) / (45 * l))

month = int((h + l + 7 * m + 114) / 32)
day = int((h + 1 - 7 * m + 114) % 31)

print(f'{day}.{month}')