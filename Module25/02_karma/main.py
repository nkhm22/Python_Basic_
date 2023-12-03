import random



class KillError():
    def __str__(self):
        return 'Убил человека'


class DrunkError():
    def __str__(self):
        return'Напился'


class CarCrashError():
    def __str__(self):
        return 'Попал в ДТП'


class GluttonyError(Exception):
    def __str__(self):
        return 'Объелся'


class DepressionError():
    def __str__(self):
        return 'Впал в депрессию'


def one_day():
    if random.randint(1, 10) != 10:
        return random.randint(1, 7)
    else:
        raise BaseException


karma = 0
while karma <= 500:
    try:
        karma += one_day()
        print(karma)
    except BaseException:
        with open('karma.log', 'w', encoding='utf-8') as errors:
            errors.write(random.choice(['Убил человека', 'Напился', 'Попал в ДТП', 'Объелся', 'Впал в депрессию']))