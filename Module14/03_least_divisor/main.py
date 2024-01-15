n=int(input('Введите число:'))
for a in range (2,n+1):
    if n % a == 0:
        break
print('Наименьший делитель, отличный от единицы:', a)
