try:
    num = int(input("Enter number: "))
except ValueError as er:
    print(er)
else:
    print(num ** 2)
print("The end")