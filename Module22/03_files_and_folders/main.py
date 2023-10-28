import os
def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1

        else:
            resul = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat[0] += resul[0]
            files_stat[1] += resul[1]
            files_stat[2] += 1
    return files_stat


path = os.path.abspath(os.path.join('..', '..', 'Module14'))

result = file_sizes(path)
print('Размер каталога (в Кб):', result[0] / 1024)
print('Количество подкаталогов:', result[2])
print('Количество файлов:', result[1])