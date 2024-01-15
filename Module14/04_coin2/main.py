import math
print('Введите координаты монетки:')
x = float(input('x:'))
y = float(input('y:'))
radius = float(input('Введите радиус:'))
if math.sqrt(x**2+y**2) <= radius:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
