year1 = int(input('Введите первый год:'))
year2 = int(input('Введите второй год:'))
if year1 > 9999 or year2 > 9999:
    print('Ошибка, введите четырехзначное число')
else:
    print('Годы от', year1, 'до', year2, ' с тремя одинаковыми цифрами:')
    for period in range (year1, year2+1):
        digit1 = period // 1000
        digit2 = period // 100 % 10
        digit3 = period // 10 % 10
        digit4 = period % 10
        if (digit1 == digit2 == digit3 or digit1 == digit2 == digit4 or digit4 == digit2 == digit3 or digit4 == digit1 == digit3) and period!=(1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999):
            print(digit1 * 1000+digit2*100+digit3*10+digit4)
