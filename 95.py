#Многие в своих сообщениях не ставят заглавные буквы, особенно если ис-
#пользуют для набора мобильные устройства. Создайте функцию, которая 
#будет принимать на вход исходную строку и возвращать строку с восста-
#новленными заглавными буквами. По существу, ваша функция должна:
# - сделать заглавной первую букву в строке, не считая пробелы;
# - сделать заглавной первую букву после точки, восклицательного или 
#вопросительного знака, не считая пробелы;
# - если текст на английском языке, сделать заглавными буквы «i», ко-
#торым предшествует пробел или за которыми следует пробел, точка, 
#восклицательный или вопросительный знак.
#Реализация такого рода автоматической корректуры исключит боль-
#шую часть ошибок с регистром букв. Например, строку «what time do i have 
#to be there? what’s the address? this time i’ll try to be on time!» ваша функция 
#должна преобразовать в более приемлемый вариант «What time do I have 
#to be there? What’s the address? This time I’ll try to be on time!». В основной 
#программе запросите у  пользователя исходную строку, обработайте ее 
#при помощи своей функции и выведите на экран итоговый результат.

def capitalize(s: str):
    result = s.replace(' i ', ' I ')

    if len(s) > 0:
        result = result[0].upper() + result[1 : len(result)]

    pos = 0
    while pos < len(s): 
        if result[pos] == '.' or result[pos] == '!' or result[pos] == '?':
            pos += 1
    
            while pos < len(s) and result[pos] == ' ':
                pos += 1

            if pos < len(s):
                result = result[0: pos] + result[pos].upper() + result[pos + 1 : len(result)]
        pos += 1 
    return result

def main():
    s = input('Enter sample text: ')
    print('You text capitalized is: {} '. format(capitalize(s)))

main()