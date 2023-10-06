import random
original=[random.randint(0,9) for _ in range(10)]
original_even=[]
original_odd=[]
for even in range(0,len(original),2):
    original_even.append(original[even])
for odd in range(1,len(original),2):
    original_odd.append(original[odd])
print('Оригинальный список:', original)
new=zip(original_even,original_odd)
new_=[]
for a in new:
    new_.append(a)
print('Новый список:', new_)