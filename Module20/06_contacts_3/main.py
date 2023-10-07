phonebook={}
while True:
    temp_phonebook=[]
    choise=int(input('Введите номер действия: 1 - Добавить контакт, 2 - Найти человека.'))
    if choise==1:
        name=input('Введите имя и фамилию нового контакта (через пробел)')
        number=int(input('Введите номер телефона:'))
        phonebook[tuple(name.split())]=number
    print('Текущий словарь контактов:', phonebook)
    if choise==2:
        surname_search=input('Введите фамилию для поиска:').title()
        for name_, number_ in phonebook.items():
            if surname_search in name_[1]:
                print(name_[0],name_[1],phonebook[name_])
            else:
                print('Такого человека нет в списке')
