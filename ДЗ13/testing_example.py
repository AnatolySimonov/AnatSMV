def calculate_credit(s, r, n):
    r = r / 12
    if s < 0 or r < 0 or n < 0:
        print('Введено отрицательное значение для  s, r или n')
    else:
        result = int(s * (r * (1 + r) ** n) / ((1 + r) ** n - 1))
        return result


class Calculator:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def mult(a, b):
        return a * b
