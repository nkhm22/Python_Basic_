name=input('Название файла:')
if name.startswith('@' or '№' or '$' or '%' or '^' or '&' or '*' or '(' or ')')==True:
    print('Ошибка: название начинается недопустимым символом.')
if name.endswith('.txt' or '.docx')==False:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
if name.startswith('@' or '№' or '$' or '%' or '^' or '&' or '*' or '(' or ')')==False and name.endswith('.txt' or '.docx')==True:
    print('Файл назван верно.')