minutes = int(input('Enter count of minutes: '))
messages = int(input('Enter count of messages: '))

total = 15.44

if minutes > 50:
    total += (minutes - 50) * 0.25
if messages > 50:
    total += (messages - 50) * 0.15

print(f'Total: ${(total * 1.05).__round__(2)}')