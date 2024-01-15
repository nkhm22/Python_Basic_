text = 'abcd'
digits = (10, 20, 30, 40)
t = [a for a in text]
d = [b for b in digits]
result = []
for c in zip(t, d):
    result.append(c)
print(result)
print(zip(t, d))