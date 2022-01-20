#Напишите программу, реализующую код Цезаря. Позвольте пользова-
#телю ввести фразу и количество символов для сдвига, после чего выведите 
#результирующее сообщение. Убедитесь в том, что ваша программа шиф-
#рует как строчные, так и прописные буквы. Также должна быть возмож-
#ность указывать отрицательный сдвиг, чтобы можно было использовать 
#вашу программу для расшифровки фраз.

message = input('Enter a mesage: ')
shift = int(input('Enter a shift value: '))

ciphered_message = ''

for character in message:
    if character >= 'a' and character <= 'z':
        pos = ord(character) - ord('a')
        pos = (pos + shift) % 26
        new_character = chr(pos + ord('a'))
        ciphered_message += new_character
    elif character >= 'A' and character <= 'Z':
        pos = ord(character) - ord('A')
        pos = (pos + shift) % 26
        new_character = chr(pos + ord('A'))
        ciphered_message += new_character
    else:
        ciphered_message += character
    
print('The Ciphered message is', ciphered_message)
