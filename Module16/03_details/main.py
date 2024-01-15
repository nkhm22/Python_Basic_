shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


detail = input('Название детали:')
detail_count = 0
price_count = 0
for sh in shop:
    for de in sh:
        if de == detail:
            detail_count += 1
            price_count += sh[1]
print('Количество деталей:', detail_count)
print('Общая стоимость:', price_count)
