shift = int(input('Сдвиг:'))
N = int(input('Введите количество элементов списка:'))
list1=[]
list2=[]
list3=[]
for number1 in range(N):
  symbol = input('Введите элемент списка:')
  list1.append(symbol)
  if number1 >= N-shift:
      list2.append(symbol)
  else:
      list3.append(symbol)
print(list1)
print(list2+list3)