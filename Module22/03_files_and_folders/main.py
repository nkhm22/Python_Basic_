import os
path='C:\\Users\\79067\\OneDrive\\Рабочий стол\\Задания Skillbox\\Python_Basic\\Module16'
def find_file(cur_path):
    files=0
    dir=0
    size=0
    for elem in os.listdir(cur_path):
        path1=os.path.abspath(elem)
        if os.path.isfile(elem):
            files+=1
            size+=os.path.getsize(elem)
        else:
            dir+=1
            find_file(path1)
    return files, dir, size
print(find_file(path))