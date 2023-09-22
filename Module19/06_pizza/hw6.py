N_orders=int(input('Введите количество заказов:'))
dict_orders= {}
for i_ord in range(N_orders):
    order = input('{0}-й заказ:'.format(i_ord+1)).title().split()
    if order[0] not in dict_orders:
        dict_orders[order[0]]={order[1]:int(order[2])}
    else:
        if order[1] in dict_orders[order[0]]:
            dict_orders[order[0]][order[1]]+=int(order[2])
        else:
            dict_orders[order[0]].update({order[1]:int(order[2])})
for client,history in dict_orders.items():
   print(client,':')
   for pizza, count in history.items():
       print('\t', pizza, ':', count)
