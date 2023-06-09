a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t = a.count(5)
print('Количество цифр 5 при первом объединении:',t)
a.remove(5)
a.remove(5)
a.remove(5)
a.extend(c)
t_ = a.count(3)
print('Количество цифр 3 при втором объединении:',t_)
print(a)