def add(a, b):
    detail.append(f"{a} + {b} = {a + b}")
    return a + b


def multi(a, b):
    detail.append(f"{a} * {b} = {a * b}")
    return a * b


def divide(a, b):
    detail.append(f"{a} / {b} = {a / b}")
    return a / b


def expo(a, b):
    detail.append(f"{a} ** {b} = {a ** b}")
    return a ** b


def subtract(a, b):
    detail.append(f"{a} - {b} = {a - b}")
    return a - b


detail = []
print("Welcome to Python Calculator App")
keep_going = True

while keep_going:
    number1 = float(input("\nEnter a number : "))
    number2 = float(input("Enter a number : "))
    operation = input("Enter an operation (addition, subtraction, divide, multiply, exponential) :")

    if operation.lower().startswith('a'):
        out = add(number1, number2)
        print(f"The sum of {number1} and {number2} is {out}")
    elif operation.lower().startswith('s'):
        out = subtract(number1, number2)
        print(f"The difference of {number1} and {number2} is {out}")
    elif operation.lower().startswith('m'):
        out = multi(number1, number2)
        print(f"The product of {number1} and {number2} is {out}")
    elif operation.lower().startswith('d'):

        if number2 == 0:
            print("you cannot divide by zero")
            detail.append("Div Error")
        else:
            out = divide(number1, number2)
            print(f"The quotient of {number1} and {number2} is {out}")
    elif operation.lower().startswith('e'):
        out = expo(number1, number2)
        print(f"The result of {number1} to the power {number2} is {out}")
    else:
        detail.append("OPP Error")
        print("That is not a valid operation")

    keep_going = input("\nWould you like to run program again (y/n) : ").lower() == 'y'

print("\nCalculation Summary :")

for i in detail:
    print(i)
print("\nThank you for using python calculator App. Goodbye")
