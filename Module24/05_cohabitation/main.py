import random
class Home:
    def __init__(self):
        self.fridge = 50
        self.money = 0
        self.l_lodger = [Human(self) for _ in range(1, 2)]


class Human:
    lst = []
    def __init__(self, other):
        self.name = ''
        self.house = other
        self.satiety = 50
        Human.lst.append(self)
    def human_enter(self):
        quantity = int(input('Введите количество людей: '))
        for _ in range(quantity):
            self.name = input('Введите имя человека: ')
            self.lst.append(self.name)
    def work(self):
        self.house.money += 1
        self.satiety -= 1
    def eat(self):
        self.satiety += 2
        self.house.fridge -= 1
    def play(self):
        self.satiety -= 1
    def shop(self):
        self.house.fridge += 2
        self.house.money -= 1
    def life_day_action(self):
        cube = random.randint(1, 6)
        return cube


home = Home()
human = Human(home)
count_day = 0
human_list = []
human.human_enter()
for __ in range(365):
    count_day += 1
    print(f'{count_day}-й день')
    if human.life_day_action() == 1:
        print('На кубике выпало 1')
        human.work()
        print('{} поработал, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
    elif human.life_day_action() == 2:
        print('На кубике выпало 2')
        human.eat()
        print('{} поел, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
    else:
        human.play()
        print('{} поиграл, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
        if human.satiety < 20:
            human.eat()
            print('{} поел, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
        if home.fridge < 10:
            human.shop()
            print('{} cходил в магазин, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
        if home.money < 50:
            human.work()
            print('{} поработал, сытость: {}, еда: {}, деньги: {}'.format(human.name, human.satiety, home.fridge, home.money))
        if human.satiety < 0:
            print('Человек умер')
            break
