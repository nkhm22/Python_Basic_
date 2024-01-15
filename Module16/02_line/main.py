def selection(list_children):
    for i in range(len(list_children)):
        for curr in range(i, len(list_children)):
            if list_children[curr] < list_children[i]:
                list_children[curr], list_children[i] = list_children[i], list_children[curr]

a = []
a.append(list(range(160, 177, 2)))
b = []
b.append(list(range(162, 181, 3)))
a.extend(b)
selection(a)
print(a)
