text=input('Введите строку:')
count = 0
length = []
for i in text.split():
    length.append(len(i))
print('Самое длинное слово:',text.split()[(length.index(max(length)))])
print('Длина этого слова:',max(length))
