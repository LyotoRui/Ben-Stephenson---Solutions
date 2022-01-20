#Расширьте свое решение упражне-ния под номером 75,
#чтобы при вынесении решения о том, является ли 
#строка палиндромом, игнорировались пробелы. Также можете поработать 
#над тем, чтобы игнорировались знаки препинания, а заглавные и пропис-
#ные буквы считались эквивалентными.

text = input('Enter a text to check if its is a palindrome: ')

new_text = ''.join(text.split())

if new_text[::-1] == new_text:
    print('Your text is a palindrome')
else:
    print('Your text is NOT a palindrome')
