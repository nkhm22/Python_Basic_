def rec_func(num):
    if num == 0:
        return 1
    else:
        rec_func(num - 1)
        return print(num)
num = int(input('Введите num:'))
rec_func(num)