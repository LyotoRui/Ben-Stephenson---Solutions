#Представьте, что сумма за пользование услугами такси складывается из 
#базового тарифа в  размере $4,00 плюс $0,25 за каждые 140 м поездки. 
#Напишите функцию, принимающую в качестве единственного параметра 
#расстояние поездки в километрах и возвращающую итоговую сумму опла-
#ты такси. В  основной программе должен демонстрироваться результат 
#вызова функции.

from posixpath import sep


RATE = 0.25
BASIC_RATE = 4

def taxi(distance: float):
    return BASIC_RATE + (RATE * ((distance * 1000) / 140)).__round__(2)

input = float(input('Enter distance in km: '))

print(
    f'Basic rate: ${BASIC_RATE}',
    f'Rate per each 140m: ${RATE}',
    f'Total cost: ${taxi(input)}',
    sep='\n'
)
