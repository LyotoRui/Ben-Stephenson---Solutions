#Напишите программу для вывода таблицы соотношения температур, вы-
#раженных в  градусах Цельсия и  Фаренгейта. В таблице должны разме-
#щаться все температуры между 0 и 100 градусами Цельсия, кратные 10. 
#Дополните таблицу подходящими заголовками. Формулу для перевода 
#температуры из градусов Цельсия в  градусы Фаренгейта можно легко 
#найти на просторах интернета.

for i in range(0, 101, 10):
    print(f'{i}C | {i * 1.8 + 32}F')