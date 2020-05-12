import math
import cmath
print("Welcome to Quadratic Equation Solver App")
print("\nA Quadratic equation is of form ax^2 + bx + c = 0")
print("Your solution can be real or complex number")
print("A Complex number  has two part: a + bj")
print("Where a is the real part and bj is the imaginary part of the number")
n = int(input("\nHow many quadratic equation would you like to solve today"))

for i in range(1,n+1):
    print(f"\nSolving equation #{i}")
    print("-------------------------------------------")
    a = float(input("\nPlease enter the value of a (co-efficent of x^2) : "))
    b = float(input("Please enter the value of b (co-efficent of x) : "))
    c = float(input("Please enter the value of c (co-efficent) : "))
    print(f"\nThe Solution of equation {a}x^2 + {b}x + {c} are :")
    d = (b**2) - (4*a*c)
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    print(f"\n\t sol1 = {sol1.real} + {sol1.imag}j")
    print(f"\tsol2 = {sol2.real} + {sol2.imag}j")
print("\nThank you for using Quadratic Solver App.  Goodbye!!")
