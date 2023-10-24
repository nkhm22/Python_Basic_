tour=open('first_tour.txt','r')
name=[]
list_2_tour=[]
for string in tour:
    name.append(string)
for elem in name:
    for ielem in elem.split():
        if ielem.isnumeric():
            if int(ielem)>int(name[0]):
                list_2_tour.append(elem)
second_tour = open('second_tour.txt', 'w')
second_tour.write(str(len(list_2_tour)))
second_tour.write('\n')
for i_elem in list_2_tour:
    second_tour.write(i_elem.split()[1][0])
    second_tour.write('. ')
    second_tour.write(i_elem.split()[0])
    second_tour.write('\t')
    second_tour.write(i_elem.split()[2])
    second_tour.write('\n')
second_tour.close()
