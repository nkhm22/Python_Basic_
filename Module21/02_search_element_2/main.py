def search_element(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for _ in range(step-1):
        for key, value in data.items():
            if isinstance(value, dict):
                result = search_element(value, tag)
                if result:
                    return result
    return result


site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}

search_key = input("Искомый ключ: ")
step=int(input('Введите максимальную глубину: '))
value = search_element(site, search_key)
if value:
    print("Значение:", value)
else:
    print("Такого ключа в структуре сайта нет.")

