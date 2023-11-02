import random
class Student():
    def __init__(self, name_surname = '', group = 1, estimation = []):
        self.name_surname = name_surname
        self.group = group
        self.estimation = estimation
    def print_stud(self):
        print('Имя и фамилия: {}, номер группы: {}, оценки: {}'.format(self.name_surname, self.group, self.estimation))
    def stud_name(self):
        self.name_surname = input('Введите имя и фамилию студента ')
        self.estimation = (random.randint(1, 5) + random.randint(1, 5) + random.randint(1, 5) + random.randint(1, 5) + random.randint(1, 5))/5

stud = Student()
names_list = []
estimations_list = []
pairs = []
quantity = int(input('Введите количество студентов: '))
for _ in range(quantity):
    stud.stud_name()
    names_list.append(stud.name_surname)
    estimations_list.append(stud.estimation)
    stud.print_stud()
for i in range(quantity):
    pairs.append((names_list[i], estimations_list[i]))
pairs.sort(key=lambda x: x[1])
print(pairs)
