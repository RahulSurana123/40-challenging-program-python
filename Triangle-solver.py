import math
print("Welcome to the Triangle Solver App\n")
base = float(input("What is the length of base of the triangle : "))
altitude = float(input("What is the length of altitude of the triangle : "))
hypotenuse = math.sqrt((base**2) + (altitude**2))
area = 1 / 2 * base * altitude
print("triangle with base " + str(base) + "and altitude " + str(altitude) + " has Hypotenus of " + str(hypotenuse) +
      " length")
print("Area of the triangle with base " + str(base) + "and altitude " + str(altitude) + " is : " + str(area))