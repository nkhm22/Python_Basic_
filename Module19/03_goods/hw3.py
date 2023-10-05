goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for lamp in store.get('12345'):
    print('Лампа —', lamp.get('quantity'), 'штук, стоимость:', lamp.get('quantity') * lamp.get('price'))
for table in store.get('23456'):
    print('Стол —', table.get('quantity'), 'штук, стоимость:', table.get('quantity') * table.get('price'))
for sofa in store.get('34567'):
    print('Диван —', sofa.get('quantity'), 'штук, стоимость:', sofa.get('quantity') * sofa.get('price'))
for chair in store.get('45678'):
    print('Стул —', chair.get('quantity'), 'штук, стоимость:', chair.get('quantity') * chair.get('price'))
