#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
#деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
#ноль.

def my_f(d_1, d_2):
    if d_2 == 0:
        print("На ноль делить нельзя!")
    else:
        div = d_1 / d_2
        print(f"Div: {div}")


my_f(int(input("d_1: ")), int(input("d_2: ")))
