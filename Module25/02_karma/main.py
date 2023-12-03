import random
class Exception:
    def __init__(self):
        self.list_error = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]


class KillError(Exception):
    def __str__(self):
        return 'Убил человека'


class DrunkError(Exception):
    def __str__(self):
        return'Напился'


class CarCrashError(Exception):
    def __str__(self):
        return 'Попал в ДТП'


class GluttonyError(Exception):
    def __str__(self):
        return 'Объелся'


class DepressionError(Exception):
    def __str__(self):
        return 'Впал в депрессию'


def one_day():
    file = open('karma.log','w')
    if random.randint(1, 10) != 10:
        return random.randint(1, 7)
    else:
        return 0
        file.write(random.choice(Exception.list_error))


karma = 0
while karma <= 500:
    karma += one_day()
    print(karma)
