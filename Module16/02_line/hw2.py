def selection(list_children):
    for i in range(len(list_children)):
        for curr in range(i, len(list_children)):
            if list_children[curr] < list_children[i]:
                list_children[curr], list_children[i] = list_children[i], list_children[curr]

a=[]
for a_ in range (160,177,2):
    a.append(a_)
b=[]
for b_ in range (162,181,3):
    a.append(a_)
a.extend(b)
selection(a)
print(a)