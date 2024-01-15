text = input('Введите текст:')
letter_h_1 = text.index('h')
letter_h_2 = text.rindex('h')
result = text[(letter_h_2-1):letter_h_1:-1]
print('Развёрнутая последовательность между первым и последним h:', result)
