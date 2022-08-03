def my_f(n):
    return n ** 3

try:
    print(my_f(int(input("Enter number: "))))
except ValueError as er:
    print(er)

print("The end")