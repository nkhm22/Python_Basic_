class Mydict(dict):
    def get(self, key, default = 0):
        return super().get(key, default)

def main():
    print('Проверки')
    my_dict = Mydict()
    my_dict['a'] = 1
    my_dict['b'] = 2
    print('Ключ a', my_dict['a'])
    print('Ключ b', my_dict['b'])
    print('Несуществующий ключ:', my_dict.get('c'))

main()