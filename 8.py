#Интернет-магазин занимается продажей различных сувениров и безде-
#лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите про-
#грамму, запрашивающую у пользователя количество тех и других покупок, 
#после чего выведите на экран общий вес посылки.

souvenir = int(input('Enter souvenirs count: '))
bouble = int(input('Enter boubles count: '))
print(f'Total weight: {souvenir * 75 + bouble * 112}g')
