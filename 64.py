from re import L


#В магазине была объявлена скидка размером 60 % на ряд товаров, и для 
#того чтобы покупатели лучше ориентировались, владелец торговой точки 
#решил вывесить отдельную таблицу со скидками с указанием уцененных 
#товаров и их оригинальных цен. Используйте цикл для создания подобной 
#таблицы, в которой будут исходные цены, суммы скидок и новые цены для 
#покупок на сумму $4,95, $9,95, $14,95, $19,95 и $24,95. Убедитесь в том, 
#что суммы скидки и  новые цены отображаются с двумя знаками после 
#запятой.

pattern = [
    4.95,
    9.95,
    14.95,
    19.95,
    24.95
]

for price in pattern:
    print(f'Old price: {price} | 60% off price: {round(price * 0.6, 2)}')
