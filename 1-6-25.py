seconds = int(input('Enter total seconds: '))

days = seconds // 86400
seconds = seconds % 86400

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print(f'{days}:{hours}:{minutes}:{seconds}')