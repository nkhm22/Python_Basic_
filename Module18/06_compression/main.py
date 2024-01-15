text = input('Введите строку:')
count_sym = 1
new_text = []
for sym in range(len(text)-1):
    if text[sym] == text[sym+1]:
        count_sym += 1
    else:
        new_text.append(text[sym])
        new_text.append(count_sym)
        count_sym = 1
print(''.join(str(x) for x in new_text))