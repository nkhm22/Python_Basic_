import random
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
result = [max(first_team[i], second_team[i]) for i in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', result)
