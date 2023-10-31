import random
class Unit():
    number = ''
    points = 100

player_1 = Unit()
player_2 = Unit()
player_1.number = '1'
player_2.number = '2'
for _ in range(11):
    command = random.randint(1, 2)
    if command == 1:
        player_2.points -= 20
        print('Атаковал игрок 1, у игрока 2 осталось {} здоровья'.format(player_2.points))
        if player_2.points <= 0:
            print('Победил игрок 1')
            break
    if command == 2:
        player_1.points -= 20
        print('Атаковал игрок 2, у игрока 1 осталось {} здоровья'.format(player_1.points))
        if player_1.points <= 0:
            print('Победил игрок 2')
            break