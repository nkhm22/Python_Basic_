with (open('registrations.txt', 'r', encoding='utf-8') as base,
      open('registrations_good.log', 'w', encoding='utf-8') as good,
      open('registrations_bad.log', 'w', encoding='utf-8') as bad):

    for elem in base:
        list_elem=elem.split()
        try:
            if len(list_elem) != 3:
                raise IndexError('Должно быть 3 поля')
            if len(list_elem[0]) < 3 and list_elem[0].isalpha() == False:
                raise NameError('Имя должно содержать только буквы и быть длиннее 2 символов')
            if ('@' and '.') not in list_elem[1]:
                raise SyntaxError('Некорректный адрес электронной почты')
            if int(list_elem[2]) < 10 or int(list_elem[2]) > 99:
                raise ValueError('Некорректный возраст')
            else:
                good.write(elem)
        except(IndexError, NameError, SyntaxError, ValueError) as error:
            bad.write(elem)
            bad.write(' ')
            bad.write(str(error))