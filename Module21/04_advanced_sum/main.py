list_question=[[1, [2, [3]], [1]], 3]
def sum_list(summ):
    su=0
    for elem in summ:
        if isinstance(elem,int):
            su+=elem
        else:
            su+=sum_list(elem)
    return su
print(sum_list(list_question))