a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t = 0
for i in a:
 if i == 5:
  t += 1
print('Количество цифр 5 при первом объединении:',t)
a.remove(5)
a.remove(5)
a.remove(5)
a.extend(c)
t_ = 0
for i in a:
 if i == 3:
  t_ += 1
print('Количество цифр 3 при втором объединении:',t_)
print(a)