N = int(input('Введите число:'))
odd = []
for a in range (1,N+1):
    if a % 2 == 1:
        odd.append(a)
print('Список из нечётных чисел от одного до N', odd)
