word = input('Введите слово:')
let=0
f_half=[]
s_half=[]
word_=[]
for letter in word:
    let+=1
    word_.append(letter)
f_half = (word_[0:(let//2)])
if let % 2 == 0:
    s_half = (word_[(let // 2):let])
else:
    s_half = (word_[((let // 2)+1):let])
s_half.reverse()
if f_half == s_half:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')