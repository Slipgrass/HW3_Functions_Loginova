def my_f(x, y):
    if y >= 0:
        sub = "undef"
    elif y < 0:
        for i in range(abs(y)):
            sub = 1
            sub = sub / x

    return sub

try:
    print(my_f(float(input("x: ")), int(input("y: "))))
except ValueError as er:
    print(er)
except NameError as er:
    print(er)


