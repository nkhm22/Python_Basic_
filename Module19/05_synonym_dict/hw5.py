def get_syn (syn_dict):
    syn_reqst=input('Введите слово:')
    if syn_reqst in syn_dict.keys():
        return syn_dict[syn_reqst]
    elif syn_reqst in syn_dict.values():
        for word in syn_dict:
            if syn_dict[word]==syn_reqst:
                return word

N=int(input('Введите количество пар слов:'))
syn_dict={}
for n in range(N):
  temp_list=[]
  print(n+1,'-я пара:', end='')
  pair = input ('').split()
  syn_dict[pair[0].lower()]=pair[1].lower()
while True:
  synonim=get_syn(syn_dict)
  if synonim:
      print('Синоним',synonim.title())
      break
  else:
      print('Такого слова в словаре нет.')