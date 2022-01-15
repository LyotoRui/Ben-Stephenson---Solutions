pattern = {
    40: 'Quiet room',
    70: 'Alarm clock',
    106: 'Gas lawm mower',
    130: 'Jackhammer'
}

noise = int(input('Enter noise level, dB: '))

if noise in pattern.keys():
    print(f'Your noise is like {pattern[noise]}.')
elif noise < 40:
    print('It`s too quite.')
elif noise in range(41, 70):
    print(f'Your noise is between {pattern[40]} and {pattern[70]}.')
elif noise in range(71, 106):
    print(f'Your noise is between {pattern[70]} and {pattern[106]}.')
elif noise in range(107, 130):
    print(f'Your noise is between {pattern[106]} and {pattern[130]}.')
else:
    print(f'You noise is too loud even for {pattern[130]}.')