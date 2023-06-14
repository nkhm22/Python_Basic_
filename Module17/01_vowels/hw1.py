text=input('Введите текст:')
letter_list=[letter for letter in text if letter=='а' or letter=='е' or letter=='и' or letter=='о' or letter=='у' or letter=='ы' or letter=='э' or letter=='ю' or letter=='я']
print('Список гласных букв:',letter_list)
print('Длина списка:',len(letter_list))