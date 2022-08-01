def my_list():
    number = 0
    while True:
        numbers_list = input("Введите целые числа или букву q для выхода из программы: ").split()
        for i in numbers_list:
            if i.lower() == 'q':
                return (f"Выход. Итоговая сумма: {number}")
            else:
                try:
                    number += int(i)
                except ValueError:
                    print("Ошибка ввода")
        print(number)

print(my_list())
