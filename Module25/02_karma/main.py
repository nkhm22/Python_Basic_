import random


class KillError(Exception):
    def __init__(self):
        super().__init__('Убил человека')


class DrunkError(Exception):
    def __init__(self):
        super().__init__('Напился')


class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Попал в ДТП')


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Объелся')


class DepressionError(Exception):
    def __init__(self):
        super().__init__('Впал в депрессию')

excs = (GluttonyError, DepressionError, CarCrashError, DrunkError, KillError)
def one_day():
    if random.randint(1, 10) != 10:
        return random.randint(1, 7)
    else:
        raise random.choice(excs)


karma = 0
with open('karma.log', 'w', encoding='utf-8') as errors:
    while karma <= 500:
        try:
            karma += one_day()
            print(karma)
        except excs as ex:
            print(ex, type(ex))
            errors.write(f'{ex}, ')