import random
digits=open('out_file.txt', 'w', encoding='utf-8')
count = 0
while True:
    digit = int(input('Введите число:'))
    if digit == random.sample(range(1, 777), int(777/14)):
        print('Вас постигла неудача!', file=digits)
        break
    count += digit
    digits.write(str(digit))
    digits.write('\n')
    if count >= 777:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
        break
digits.close()
