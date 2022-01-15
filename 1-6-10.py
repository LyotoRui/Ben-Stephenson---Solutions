from math import log10

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(
    a + b,
    a - b,
    a * b,
    a / b,
    a % b,
    log10(a),
    a ** b,
    sep='\n'
    )