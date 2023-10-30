your_name = input('Введите Ваш логин:')
while True:
    chat = open('history.txt', 'a', encoding='utf-8')
    command = input('Введите команду(1. Посмотреть текущий текст чата, 2. Отправить сообщение):')
    if command == '2':
        massage = input('Введите сообщение:')
        chat.write(your_name)
        chat.write(':')
        chat.write(massage)
        chat.write('\n')
    if command == '1':
        chat_read = open('history.txt', 'r', encoding='utf-8')
        print(chat_read.read())