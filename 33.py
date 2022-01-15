nums = [
    int(input('Enter first number: ')),
    int(input('Enter second number: ')),
    int(input('Enter third number: '))
]

for i, item in zip(range(1, 4), sorted(nums)):
    print(f'{i} - {item}')