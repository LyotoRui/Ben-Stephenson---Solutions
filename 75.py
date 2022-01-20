#Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, яв-
#ляется ли она палиндромом.

word = input('Enter a word to check if its is a palindrome: ')

if len(word) == 1:
    print('You cannot check if a letter is a palindrome')
else:
    if word[::-1] == word:  
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')