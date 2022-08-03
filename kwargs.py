def my_f(**kwargs):
    return kwargs


#print(my_f(n=1, m=2, v=3))
#print(my_f(int(input("s_1: ")), int(input("s_2: ")))**2)
print(my_f(name='Jack', surname='Smith', year=2012, city='Moskow', email='smith@mail.ru', phone='+7(812)345647'))