import math
print("Welcome to Factorial Calculator App")


def fac(no):

    if no == 1:
        print(str(no))
        return 1
    print(str(no) + " *", end=" ")
    return no * fac(no - 1)


n = int(input("\nWhat number's factorial would you like to find ?"))
print("\n" + str(n) + "! = ", end=" ")

value = fac(n)
print("\nThe factorial of " + str(n) + " using math lib is : ", end ="")
print(math.factorial(n))

print("\nThe factorial of " + str(n)+" using our calculator is : " + str(value))
