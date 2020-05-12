print("Welcome to temp converter App\n")
fahrenheit = float(input("What is the temperature in degree fahrenheit :"))
celsius = 5 / 9 * (fahrenheit - 32)
kelvin = celsius + 273
print("Degrees Fahrenheit : " + str(fahrenheit))
print("Degrees Celsius : " + str(round(celsius, 4)))
print("Degrees kelvin : " + str(round(kelvin, 4)))
