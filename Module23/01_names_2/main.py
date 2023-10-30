with (open('people.txt', 'r', encoding='utf-8') as people,
open('stats.txt', 'w', encoding='utf-8') as statistics):
    line_count = 0
    sym = 0
    try:
        for line in people:
            line_count += 1
            sym += len(line.strip())
            if len(line.strip()) < 3:
                raise BaseException
    except BaseException:
        print('Менее трёх символов в строке {}'.format(line_count), file = statistics)
    print('Общее количество символов:', sym, file = statistics)