def tpl_sort(tpl_p):
    for i in tpl_p:
        if not isinstance(i, int):
            return tpl_p
    sorted_list=sorted(list(tpl_p))
    sorted_tpl=tuple(sorted_list)
    return sorted_tpl
tpl = (6, 3.9, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))