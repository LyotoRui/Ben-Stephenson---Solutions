#Напишите программу, использующую для подброса монетки генера-
#тор случайных чисел Python. Монетка при этом должна быть правильной 
#формы, что означает равную вероятность выпадения орла и решки. Под-
#брасывать монетку необходимо до тех пор, пока три раза подряд не вы-
#падет одно значение, вне зависимости от того, орел это будет или решка. 
#Выводите на экран букву О всякий раз, когда выпадает орел, и Р – когда 
#выпадает решка. При этом для одной симуляции бросков все выпавшие 
#значения необходимо размещать на одной строке. Также необходимо из-
#вестить пользователя о том, сколько попыток потребовалось, чтобы полу-
#чить нужный результат.

from random import randrange

eagles = 0
tails = 0
attempts_list = []
attempts = 0

for i in range(10):
    while eagles < 3 or tails < 3:
        shot = randrange(1, 3)
        if shot == 1:
            eagles += 1
        else:
            tails += 1
        attempts += 1
    attempts_list.append(attempts)
    print(f'Number of tries: {attempts}')
    eagles = 0
    tails = 0
    attempts = 0

print(f'Mean count of attempts: {sum(attempts_list) / len(attempts_list).__round__(2)}')