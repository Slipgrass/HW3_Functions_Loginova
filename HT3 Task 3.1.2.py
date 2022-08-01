def my_f(d_1, d_2):
    return d_1 / d_2

try:
    print(my_f(int(input("d_1: ")), int(input("d_2: "))))
except ValueError as er:
    print(er)
    """Реагирует на неверный ввод, если введено не число, а строка"""
except ZeroDivisionError as er:
    print(er)
    """Реагирует на 0 в делителе"""

