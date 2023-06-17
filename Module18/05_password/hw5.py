password = input('Придумайте пароль:')
while True:
    if len(password)>=8 and len([letter for letter in password if letter.isupper()])!=0 and sum(c.isdigit() for c in password)>=3:
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input('Придумайте пароль:')

