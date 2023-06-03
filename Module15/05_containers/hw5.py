quantity=int(input('Количество контейнеров:'))
container_list=[]
for number in range(quantity):
  weight=int(input('Введите вес контейнера:'))
  if weight>200:
    print('Ошибка, вес контейнера должен быть не более 200 кг')
    break
  container_list.append(weight)
if weight <= 200:
  new_container=int(input('Введите вес нового контейнера:'))
for w in range (quantity):
  if container_list[w] < new_container:
     break
print('Номер, который получит новый контейнер:',w+1)


