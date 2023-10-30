import math
def get_sage_sqrt(digit):
    try:
        if isinstance(digit, str):
            raise TypeError('Элемент не является числом')
        if digit <= 0:
            raise ValueError('Нельзя извлечь квадратный корень из отрицательного числа и 0')
        res = math.sqrt(digit)
        return res
    except TypeError as exc:
        print(exc)
    except Exception as exc:
        print(exc)
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    if isinstance(result, float) or isinstance(result, int):
        print(f"Квадратный корень numbers {number}: {result}")