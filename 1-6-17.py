mass = int(input('Enter mass of the coffee, g: '))
current_temp = int(input('Enter current temp, C: '))
needed_temp = int(input('Enter needed temp, C: '))
energy = mass * 4.186 * (needed_temp - current_temp)

print(
    f'Energy needed, joule: {energy}',
    f'Energy cost, $: {(energy / 3.6e+6) * 0.089}',
    sep='\n'
)