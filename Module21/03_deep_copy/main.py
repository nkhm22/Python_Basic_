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
def deep_copy(object):
    if isinstance(object, (int, float, str)):
        return object
    elif isinstance(object, (list)):
        return[deep_copy(item) for item in object]
    elif isinstance(object, (dict)):
        return {key: deep_copy(value) for key, value in object.items()}
    else:
        return copy.deepcopy(object)

def find_key(strukture, key):
    if key in strukture:
        return strukture[key]
    for substruct in strukture.values():
        if isinstance (substruct,dict):
            result = find_key(substruct,key)
            print('0', result)
            result = 'Куплю\продам {} недорого'.format(product)
            substruct[key]=result
            print('1', result)
            if result:
                break
    else:
        result=None
    return strukture

sites=int(input('Сколько сайтов?'))
count=1
site_list=[]
while count<=sites:
    product=input('Введите название продукта для нового сайта: ')
    productes_sait=deep_copy(site)
    print('Копия:')
    count+=1
    value=find_key(site, 'title')
    if value:
        print('Сайт для {}:'.format(product), 'site', value)