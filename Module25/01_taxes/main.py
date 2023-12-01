class Property:
    cost = 0
    worth = float(input('Введите количество денег: '))
    def tax(self, size):
        dimension = self.cost * size
        return dimension


class Apartment(Property):
    cost = float(input('Введите стоимость квартиры: '))
    def print_tax(self):
        return super().tax(size = 0.001)


class Car(Property):
    cost = float(input('Введите стоимость машины: '))
    def print_tax(self):
        return super().tax(size=0.005)


class CountryHouse(Property):
    cost = float(input('Введите стоимость дачи: '))
    def print_tax(self):
        return super().tax(size=0.002)

property = Property()
apartment = Apartment()
car = Car()
countryhouse = CountryHouse()
if property.worth - apartment.print_tax() - car.print_tax() - countryhouse.print_tax() >= 0:
    print('Денег достаточно')
else:
    print(f'Денег недостаточно, добавьте {apartment.print_tax() + car.print_tax() + countryhouse.print_tax() - property.worth}')
