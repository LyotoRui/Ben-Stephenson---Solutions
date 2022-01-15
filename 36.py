age = int(input('Enter dog`s age: '))

if age > 0:
    if age > 2:
        print(f'Your dog is {(age - 2) * 4 + 21} human years old.')
    else:
        print(f'Your dog is {age * 10.5} human years old.')
else:
    print('Your dog doesn`t exists! =)')