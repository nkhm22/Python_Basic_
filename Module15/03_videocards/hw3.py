vс_quantity=int(input('Количество видеокарт:'))
vc_list=[]
for number in range(1,vс_quantity+1):
  print('Видеокарта',number,':', end='\t')
  vc=int(input())
  vc_list.append(vc)
print('Старый список видеокарт:',vc_list)
old_version=max(vc_list)
vc_list.remove(old_version)
old_version_=max(vc_list)
vc_list.remove(old_version_)
print('Новый список видеокарт:',vc_list)