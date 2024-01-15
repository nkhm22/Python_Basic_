while True:
    IP = input('Введите IP:')
    for i in IP.split('.'):
        if i.isdigit() == False:
            print(i, '— это не целое число')
        elif int(i) > 255:
            print(i, 'превышает 255')
        elif ','.find(i) == True:
            print('Адрес — это четыре числа, разделённые точками.')
        else:
            print('IP-адрес корректен.')
            break