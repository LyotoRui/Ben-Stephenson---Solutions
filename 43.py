#В предыдущем упражнении мы определяли частоту ноты по ее назва-
#нию и номеру октавы. Теперь выполним обратную операцию. Запроси-
#те у пользователя частоту звука. Если введенное значение укладывается 
#в диапазон ±1 Гц от значения в таблице, выведите на экран название 
#соответствующей ноты. В  противном случае сообщите пользователю, 
#что ноты, соответствующей введенной частоте, не существует. В данном 
#упражнении можно ограничиться только нотами, приведенными в табли-
#це. Нет необходимости брать в расчет другие октавы.

frequency = float(input('Enter a frequencyin Hertz to find the corresponding musical note note: '))

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if B4 - 1 <= frequency <= B4 + 1:
    note = 'B4'
elif A4 - 1 <= frequency <= A4 + 1:
    note = 'A4'
elif G4 - 1 <= frequency <= G4 + 1:
    note = 'G4'
elif F4 - 1 <= frequency <= F4 + 1:
    note = 'F4'
elif E4 - 1 <= frequency <= E4 + 1:
    note = 'E4'
elif D4 - 1 <= frequency <= D4 + 1:
    note = 'D4'
elif C4 - 1 <= frequency <= C4 + 1:
    note = 'C4'
else:
    print('Enter a valid frequency!')

print(f'The frequency {frequency} corresponds to the musical note {note}')