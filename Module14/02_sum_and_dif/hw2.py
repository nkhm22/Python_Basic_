N=int(input('Введите число:'))
a=N
summ=0
while N > 0:
  summ += N % 10
  N //= 10
print('Сумма чисел:',summ)
print('Количество цифр в числе:',len(str(a)))
print('Разность суммы и количества цифр:',summ-len(str(a)))