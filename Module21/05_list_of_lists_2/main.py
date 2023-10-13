list_question=[1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
def sum_list(summ):
    if summ==[]:
        return summ
    if isinstance(summ[0],list):
        return (sum_list(summ[0])+sum_list(summ[1:]))
    return(summ[:1]+sum_list(summ[1:]))
print(sum_list(list_question))