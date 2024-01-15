N = int(input('Введите длину списка:'))
n_list = list(range(N))
n_list_new = [(1 if i % 2 == 0 else i % 5) for i in n_list]
print(n_list_new)