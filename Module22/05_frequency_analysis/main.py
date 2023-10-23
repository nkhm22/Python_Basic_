text=open('text.txt', 'r')
analysis=open('analysis.txt', 'w')
frequency = {}
for line in text:
    for symbol in line:
        if symbol!=' ':
            if symbol in frequency:
                frequency[symbol] += 1
            else:
                frequency[symbol] = 1

    for letter, freq in frequency.items():
        print(letter, ':', round(float(freq/len(line)), 3))
        analysis.write(letter)
        analysis.write(' : ')
        analysis.write(str(round(float(freq/len(line)), 3)))
        analysis.write('\n')
