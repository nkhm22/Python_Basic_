list_hoar=[5, 8, 9, 4, 2, 9, 1, 8]
def hoar(sequence):
    big=[]
    little=[]
    middle=[]
    if len(sequence)<=1:
        return sequence
    else:
        for elem in sequence:
            if elem>sequence[len(sequence)-1]:
                big.append(elem)
            if elem < sequence[len(sequence)-1]:
                little.append(elem)
            if elem == sequence[len(sequence)-1]:
                middle.append(elem)
        return hoar(little) + middle + hoar(big)
print(hoar(list_hoar))

