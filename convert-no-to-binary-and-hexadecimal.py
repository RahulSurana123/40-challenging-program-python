print("Welcome to Binary/Hexadecimal Converter App")
number = int(input("\nCompute binary and hexadecimal value up to following decimal number : "))
numbers = []
binarys = []
hexas = []
for i in range(1, number+1):
    numbers.append(i)
    binarys.append(bin(i))
    hexas.append(hex(i))

print("Generating lists.... complete !")
print("\nUsing slices, we will now show a portion of each list")
low_limit = int(input("What decimal number would you like to start at : ")) - 1
high_limit = int(input("What decimal number would you like to stop at : "))
print("\nDecimal value from " + str(low_limit+1) + " to " + str(high_limit) + " :")
for i in range(low_limit, high_limit):
    print(i)
print("\nbinary value from " + str(low_limit+1) + " to " + str(high_limit) + " :")
for i in range(low_limit, high_limit):
    print(bin(i))
print("\nHexadecimal value from " + str(low_limit+1) + " to " + str(high_limit) + " :")
for i in range(low_limit, high_limit):
    print(hex(i))

input("Press Enter if you want to see all the values till " + str(number))
for i, j, k in zip(numbers, binarys, hexas):
    print(str(i) + "...." + str(j) + "...." + str(k))