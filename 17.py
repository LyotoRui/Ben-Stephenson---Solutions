#Напишите программу, запрашивающую у  пользователя массу воды 
#и требуемую разницу температур. На выходе вы должны получить коли-
#чество энергии, которое необходимо добавить или отнять для достижения 
#желаемого температурного изменения.
#Расширьте свою программу таким образом, чтобы выводилась так-
#же стоимость сопутствующего нагрева воды. Обычно принято измерять 
#электричество в кВт·ч, а не в джоулях. Для данного примера предположим, 
#что электричество обходится нам в 8,9 цента за один кВт·ч. Используйте 
#свою программу для подсчета стоимости нагрева одной чашки кофе.

mass = int(input('Enter mass of the coffee, g: '))
current_temp = int(input('Enter current temp, C: '))
needed_temp = int(input('Enter needed temp, C: '))
energy = mass * 4.186 * (needed_temp - current_temp)

print(
    f'Energy needed, joule: {energy}',
    f'Energy cost, $: {(energy / 3.6e+6) * 0.089}',
    sep='\n'
)
