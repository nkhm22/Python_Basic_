N1 = input('Первая строка:')
N2 = input('Вторая строка:')
shift=0
N2_1=[]
N2_2=[]
while N1!=(N2_2+N2_1):
    N2_1 = N2[:shift]
    N2_2 = N2[shift:len(N1) + 1]
    shift+=1
print(shift)
print(N2_2+N2_1)