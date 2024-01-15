text=input('Введите текст:')
letter_list=[letter for letter in text if letter in 'аеиоуыэюя']
print('Список гласных букв:', letter_list)
print('Длина списка:', len(letter_list))