pattern = {
    'C': 130.81,
    'D': 146.83,
    'E': 164.81,
    'F': 174.61,
    'G': 196,
    'A': 220,
    'B': 246.94
}

note = input('Enter note and octave: ')
if note[1] == '0':
    print(f'Frequency of your note is {pattern[note[0].capitalize()]}')
else:
    frequency = pattern[note[0].capitalize()]
    for i in range(int(note[1])):
        frequency *= 2
    print(f'Frequency of your note is {frequency}')
