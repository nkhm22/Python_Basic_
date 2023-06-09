guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
count = 0
while True:
 command = input('Гость пришёл или ушёл?')
 if command == 'пришёл':
    new_guest = input('Имя гостя:')
    guests.append(new_guest)
    count = len (guests)
    print('Сейчас на вечеринке', count, 'человек(а):', guests)
    if count <= 6:
        print('Имя гостя:', new_guest)
        print('Привет,',new_guest)
    else:
        print('Прости,', new_guest, 'но мест нет')
 if command == 'ушёл':
    remove_guest = input('Имя гостя:')
    guests.remove(remove_guest)
    count += len (guests)
    print('Сейчас на вечеринке', count, 'человек(а):', guests)
 if command == 'Пора спать':
    print('Вечеринка закончилась, все легли спать.')
    break
