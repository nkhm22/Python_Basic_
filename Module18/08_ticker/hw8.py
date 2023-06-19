first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')

len_first = len(first_string)

for change in range(1, len_first + 1):
    new_second = second_string[-change:] + second_string[:-change]
    if new_second == first_string:
        print('Первая строка получается из второй со сдвигом', change)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')