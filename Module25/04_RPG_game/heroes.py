class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        pass

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class Healer(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - 1.2 * damage)
        super().take_damage(damage)

    def hill(self, target):
        target.set_hp(target.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() == min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()
        if min_health <= 100:
            print('Исцеляю:', target_of_potion.name)
            self.hill(target_of_potion)
        else:
            if not enemies:
                return
            print('Атакую ближнего:', enemies[0])
            self.attack(enemies[0])
        print('\n')

    def __str__(self):
        return super().__str__()
     # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель


class Tank(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = False

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)

    def set_shield_state(self):
        if self.shield:
            self.shield = False
            self.defense = self.defense / 2
            self.set_power(self.get_power() * 2)
        else:
            self.shield = True
            self.defense = self.defense * 2
            self.set_power(self.get_power() / 2)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        print(self.name, end=' ')
        if self.get_hp() < 90 and not self.shield:
            self.set_shield_state()
        elif self.get_hp() > 90 and self.shield:
            self.set_shield_state()
        else:
            target = enemies[0]
            min_health = target.get_hp()
            for enemy in enemies:
                if enemy.get_hp() < min_health:
                    target = enemy
                    min_health = enemy.get_hp()
            print('Атакую ближнего -', target.name)
            self.attack(target)
            print('\n')

    def __str__(self):
        return super().__str__() + f" | {self.shield}"

# Танк:
# Атрибуты:
# - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
# - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
# Методы:
# - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
# - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
# - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
# - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
# - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
# поднять щит/опустить щит) на выбранную им цель


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 3

    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def power_down(self):
        self.power_multiply = self.power_multiply / 2

    def power_up(self):
        self.power_multiply = self.power_multiply * 2

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * (self.power_multiply / 2)))
        super().take_damage(damage)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        print(self.name, end=' ')

        if self.power_multiply < 4:
            self.power_up()
            return

        target = enemies[0]
        min_health = target.get_hp()

        for enemy in enemies:
            if enemy.get_hp() < min_health:
                target = enemy
                min_health = enemy.get_hp()
        print('Атакую ближнего -', target.name)
        self.attack(target)
        print('\n')

    def __str__(self):
        return super().__str__()

    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
