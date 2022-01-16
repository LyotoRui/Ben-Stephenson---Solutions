#Создайте программу, в которой пользователь сможет ввести временной 
#промежуток в виде количества дней, часов, минут и секунд и узнать общее 
#количество секунд, составляющее введенный отрезок.

days = int(input('Enter days: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
seconds = int(input('Enter seconds: '))

total_sec = days * 86400 + hours * 3600 + minutes * 60 + seconds

print(f'Total in seconds: {total_sec}')