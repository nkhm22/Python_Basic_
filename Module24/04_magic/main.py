class Mud:
    answer = "Вы сложили Воду и Землю получили класс Грязь"


class Water:
    def __add__(self, left):
        if type(left) == Soil:
            return Mud()


class Soil:
    def __add__(self, left):
        if type(left) == Water:
            return Mud()


print((Water()+Soil()).answer)


class Steam:
    answer = "Вы сложили Воду и Огонь получили класс Пар"


class Water:
    def __add__(self, left):
        if type(left) == Fire:
            return Steam()


class Fire:
    def __add__(self, left):
        if type(left) == Water:
            return Steam()


print((Water() + Fire()).answer)


class Storm:
    answer = "Вы сложили Воду и Воздух получили класс Шторм"


class Water:
    def __add__(self, left):
        if type(left) == Air:
            return Storm()


class Air:
    def __add__(self, left):
        if type(left) == Water:
            return Storm()


print((Water() + Air()).answer)


class Lightning:
    answer = "Вы сложили Огонь и Воздух получили класс Молния"


class Fire:
    def __add__(self, left):
        if type(left) == Air:
            return Lightning()


class Air:
    def __add__(self, left):
        if type(left) == Fire:
            return Lightning()


print((Fire() + Air()).answer)


class Dust:
    answer = "Вы сложили Земля и Воздух получили класс Пыль"


class Soil:
    def __add__(self, left):
        if type(left) == Air:
            return Dust()


class Air:
    def __add__(self, left):
        if type(left) == Soil:
            return Dust()


print((Soil() + Air()).answer)


class Lava:
    answer = "Вы сложили Земля и Огонь получили класс Лава"


class Soil:
    def __add__(self, left):
        if type(left) == Fire:
            return Lava()


class Fire:
    def __add__(self, left):
        if type(left) == Soil:
            return Lava()


print((Soil() + Fire()).answer)
