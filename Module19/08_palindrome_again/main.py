def ispoly(str):
    char_dict = {}
    for i in str:
        char_dict[i] = char_dict.get(i, 0) + 1
    odd_count = 0
    for ii in char_dict.values():
        if ii % 2 != 0:
            odd_count += 1
    return odd_count <= 1

text = input('Введите строку:')
if ispoly(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')