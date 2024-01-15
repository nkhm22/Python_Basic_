def selection(list_digits_):
    for i in range(len(list_digits_)):
        for curr in range(i,len(list_digits_)):
            if list_digits_[curr]<list_digits_[i]:
                list_digits_[curr],list_digits_[i]=list_digits_[i],list_digits_[curr]

N = int(input('Введите количество элементов списка:'))
list_digits=[]
for number in range(N):
    digit = float(input('Введите элемент списка:'))
    list_digits.append(digit)
print(list_digits)
selection(list_digits)
print(list_digits)
