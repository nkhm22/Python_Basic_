a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)



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
