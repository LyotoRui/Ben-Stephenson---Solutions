#В данном упражнении вы создадите программу для отображения стан-
#дартной таблицы умножения от единицы до десяти.

print("    ", end='')

for i in range(1, 11):
    print('%4d' % i, end=''. format())
print()

for i in range(1, 11):
    print('%4d' % i, end='')
    for j in range(1, 11):
        print('%4d' % (i*j), end='')
    print()