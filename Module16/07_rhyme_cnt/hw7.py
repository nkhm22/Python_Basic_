N = int(input('Количество человек:'))
K = int(input('Какое число в считалке?'))
print('Значит, выбывает каждый',K,'-й человек')
n_list = list(range(1,N+1))
start=0
count = (K % N)
print(n_list)
while len(n_list)>1:
    if len(n_list)>=K:
        del n_list[N%K]
        print(n_list)
    elif len(n_list) == K:
        del n_list[K]
        print(n_list)
    else:
        del n_list[(K % len(n_list))-1]
        print(n_list)