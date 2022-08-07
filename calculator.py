def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def division(x, y):
    return x/y


while True:

    val = int(input(
        " ********************\nSelect operation :\n 1. add\n 2. Subtract\n 3. multiply\n 4. divid\n"))
    if val in (1, 2, 3, 4):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        if val == 1:
            print(add(num1, num2))
        elif val == 2:
            print(subtract(num1, num2))
        elif val == 3:
            print(multiply(num1, num2))
        elif val == 4:
            print(division(num1, num2))

    else:
        print('Invalid')
