quantity_skates=int(input('Количество коньков:'))
qs=[]
for q_s in range(quantity_skates):
    q_skates=int(input('Размер пары:'))
    qs.append(q_skates)
quantity_man=int(input('Количество людей:'))
qm=[]
for q_m in range(quantity_man):
    q_man=int(input('Размер ноги человека:'))
    qm.append(q_man)
count=0
for skates in qs:
    for man in qm:
        if skates == man:
            count+=1
print('Наибольшее количество людей, которые могут взять ролики:',count)