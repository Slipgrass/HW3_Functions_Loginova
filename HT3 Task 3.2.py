#Выполнить функцию, которая принимает несколько параметров, описывающих данные
#пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
#должна принимать параметры как именованные аргументы. Осуществить вывод данных о
#пользователе одной строкой.
def my_f(**kwargs):
    return kwargs


print(my_f(name='Jack', surname='Smith', year=2012, city='Moskow', email='smith@mail.ru', phone='+7(812)345647'))