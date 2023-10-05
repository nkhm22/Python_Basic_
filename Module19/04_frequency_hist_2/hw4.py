text = input("Введите текст: ")
frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1
list_letters1 = []
list_letters2 = []
list_letters3 = []
for letter, freq in frequency.items():
    frequency_ = {}
    frequency_.update({freq: letter})
    if freq == 1:
        list_letters1.append(letter)
    if freq == 2:
        list_letters2.append(letter)
    if freq == 3:
        list_letters3.append(letter)
print('1:', list_letters1)
print('2:', list_letters2)
print('3:', list_letters3)
