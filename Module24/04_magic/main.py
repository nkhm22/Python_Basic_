class Water:
    list_water = ['Воздух', 'Огонь', 'Земля']

    name = "Вода"

    def add(self, other):
        if other in Water.list_water:
            if other == 'Воздух':
                return print(f'Из магии Воды и магии Воздуха мы получили магию Шторм')
            if other == 'Огонь':
                return print(f'Из магии Воды и магии Огня мы получили магию Пар')
            if other == 'Земля':
                return print(f'Из магии Воды и магии Земля мы получили магию Грязь')
        else:
            return None

    def print_info(self):
        return print(f'Эта магия: {Water.name}')


class Fire:
    list_fire = ['Земля', 'Вода', 'Воздух']
    name = "Огонь"

    def add(self, other):
        if other in Fire.list_fire:
            if other == 'Воздух':
                return print(f'Из магии Огня и магии Воздуха мы получили магию Молния')
            if other == 'Вода':
                return print(f'Из магии Огня и магии Воды мы получили магию Пар')
            if other == 'Земля':
                return print(f'Из магии Огня и магии Земли мы получили магию Лава')
        else:
            return None
    def print_info(self):
        return print(f'Эта магия: {Fire.name}')
class Earth:
    list_earth = ['Огонь', 'Вода', 'Воздух']
    name = "Земля"

    def add(self, other):
        if other in Earth.earth:
            if other == 'Воздух':
                return print(f'Из магии Земля и магии Воздух мы получили магию Пыль')
            if other == 'Вода':
                return print(f'Из магии Земля и магии Воды мы получили магию Грязь')
            if other == 'Огонь':
                return print(f'Из магии Огня и магии Земли мы получили магию Лава')
        else:
            return None
    def print_info(self):
        return print(f'Эта магия: {Earth.name}')
class Air:
    list_air = ['Огонь', 'Вода', 'Земля']
    name = "Воздух"

    def add(self, other):
        if other in Air.list_air:
            if other == 'Земля':
                return print(f'Из магии Земля и магии Воздух мы получили магию Пыль')
            if other == 'Вода':
                return print(f'Из магии Воды и магии Воздуха мы получили магию Шторм')
            if other == 'Огонь':
                return print(f'Из магии Огня и магии Земли мы получили магию Лава')
        else:
            return None

    def print_info(self):
        return print(f'Эта магия: {Air.name}')