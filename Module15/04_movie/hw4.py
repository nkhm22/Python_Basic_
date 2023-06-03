films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
quantity=int(input('Сколько фильмов хотите добавить?'))
favorite_films = []
for _ in range(quantity):
  title = input('Введите название фильма:')
  if title == films[0] or title == films[1] or title == films[2] or title == films[3] or title == films[4] or title == films[5] or title == films[6] or title == films[7]:
   favorite_films.append(title)
  else:
   print('Ошибка: фильма',title,'у нас нет :(')
print('Ваш список любимых фильмов:',favorite_films)