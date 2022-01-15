foot = int(input('Enter a number: '))

print(
    f'Inches: {foot * 12}',
    f'Yards: {(foot * 0.333333).__round__(2)}',
    f'Miles: {(foot * 0.000189394).__round__(2)}',
    sep='\n'
)