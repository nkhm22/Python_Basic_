N = int(input('Количество человек:'))
K = int(input('Какое число в считалке?'))
print('Значит, выбывает каждый',K,'-й человек')

people_list = list(range(1, N + 1))

index_del = 0
while len(people_list) > 1:
    print('Текущий круг людей:', people_list)
    index_start = index_del % len(people_list)
    print('Начало счёта с номера', people_list[index_start])

    index_del = (index_start + K - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[index_del])
    people_list.remove(people_list[index_del])

print('\nОстался человек под номером', people_list[0])

