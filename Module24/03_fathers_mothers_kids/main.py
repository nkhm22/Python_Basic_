import random
class Parent():
    def __init__(self, name_parent = '', age_parent = 21, children_list = []):
        self.name_parent = name_parent
        self.age_parent = age_parent
        self.children_list = children_list
    def parent_enter(self):
        self.name_parent = input('Введите имя родителя: ')
        self.age_parent = input('Введите возраст родителя: ')
        quantity = int(input('Введите количество детей: '))
        for _ in range(quantity):
            children = input('Введите имя ребенка: ')
            self.children_list.append(children)
    def print_parent(self):
        print('Имя родителя: {}, возраст родителя: {}, дети: {}'.format(self.name_parent, self.age_parent, self.children_list))
class Child():
    def __init__(self, name_child = '', age_child = int, calm_status = random.choice([True, False]), hunger_status = random.choice([True, False])):
        self.name_child = name_child
        self.age_child = age_child
        self.calm_status = calm_status
        self.hunger_status = hunger_status
    def action(self):
        self.calm_status = random.choice([True, False])
        if self.calm_status == False:
            calm_command = input('Успокойте ребенка (+)')
            if calm_command == '+':
                print('Ребенок спокоен')
        else:
            print('Ребенок спокоен')
        self.hunger_status = random.choice([True, False])
        if self.hunger_status == True:
            hunger_command = input('Накормите ребенка (+)')
            if hunger_command == '+':
                print('Ребенок наелся')
        else:
            print('Ребенок наелся')

parent = Parent()
сhild = Child()
parent.parent_enter()
parent.print_parent()
for name_ch in parent.children_list:
    сhild.name_child = parent.children_list
    сhild.age_child = int(input('Введите возраст {}: '.format(name_ch)))
    if int(parent.age_parent) - int(сhild.age_child) < 16:
        print('Проверьте возраст ребенка')
        сhild.age_child = int(input('Введите возраст {}: '.format(name_ch)))
    сhild.action()