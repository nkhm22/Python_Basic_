import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
def search(struct,key,value):
    if key in struct:
        struct[key]=value
        return site_copy
    for i in struct.values():
        if isinstance(i,dict):
            result=search(i, key, value)
            if result:
                return site_copy
site_copy=copy.deepcopy(site)
for _ in range(int(input('Сколько сайтов?'))):
    name=input('Название продукта:')
    keys={'title': 'Куплю/продам {n} недорого'.format(n=name),
          'h2': 'У нас самая низкая цена на {n}'.format(n=name)}
    for i_key in keys:
        search(site_copy,i_key, keys[i_key])
    print(f'Сайт для {name}')
    print('site=', site_copy)
