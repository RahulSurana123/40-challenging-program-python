print("Welcome to multiplication and exponential classes\n")
name = input("What is your name young boy ? ")
print("Hii " + name.strip().title() +"!!")
number = float(input("Which number would u like to know tables of "))
print("Multiplication tables for number " + str(number) + "\n")
for i in range(1, 11):
    print("\t" + str(number) + " * " + str(i) + "  =  " + str(number * i))
print("\n\nExponential tables for number " + str(number) + "\n")
for i in range(1, 11):
    print("\t" + str(number) + " ** " + str(i) + "  =  " + str(number ** i))
