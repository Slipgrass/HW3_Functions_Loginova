def my_f(s_1, s_2, s_3):
    sub = sum({s_1, s_2, s_3}) - min(s_1, s_2, s_3)
    return sub


print(my_f(int(input("s_1: ")), int(input("s_2: ")), (int(input("s_3: ")))))