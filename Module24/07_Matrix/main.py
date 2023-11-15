class Matrix:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.data = []
    def __str__(self):
        res = ''
        for elem in self.data:
            res += '\t'.join(str(el) for el in elem)
            res += '\n'
        return res
    def add(self, new_matrix):
        res = [[self.data[l][c] + new_matrix.data[l][c] for c in range(self.column)] for l in range(self.line)]
        result = ''
        for elem in res:
            result += '\t'.join(str(el) for el in elem)
            result += '\n'
        return result
    def subtract(self, new_matrix):
        res = [[self.data[l][c] - new_matrix.data[l][c] for c in range(self.column)] for l in range(self.line)]
        result = ''
        for elem in res:
            result += '\t'.join(str(el) for el in elem)
            result += '\n'
        return result
    def multiply(self, new_matrix):
        res = [[sum(a * b for a, b in zip(A_line, B_column)) for B_column in zip(*new_matrix.data)] for A_line in self.data]
        result = ''
        for elem in res:
            result += '\t'.join(str(el) for el in elem)
            result += '\n'
        return result
    def transpose(self):
        res = [[row[i] for row in self.data] for i in range(self.column)]
        result = ''
        for elem in res:
            result += '\t'.join(str(el) for el in elem)
            result += '\n'
        return result
# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())