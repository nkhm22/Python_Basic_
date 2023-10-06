text = input('Введите текст:')

txt = []
for letter in text:
    txt.append(letter)


def is_prime():
    prime = []
    for digit in range(2, len(txt)):
        k = 0
        for i in range(2, digit // 2 + 1):
            if digit % i == 0:
                k = k + 1
        if (k <= 0):
            prime.append(digit)
    return prime


def zip_sym():
    res = []
    for number in is_prime():
        res.append(txt[number])
    return res


print(zip_sym())
# TODO здесь писать код
