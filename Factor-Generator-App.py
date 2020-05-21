print("Welcome to Factor Generator App")

flag = True
while flag:
    number = int(input("\nEnter a number to determine all the factor of that number : "))
    print(F"\nfactor of {number} are :")
    factors = [ ]
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            print(i)
    print("In Summary :")
    length_factor = int(len(factors) / 2) if len(factors) % 2 == 0 else int(len(factors) / 2 + 1)
    for m in range(length_factor):
        print(f"{factors[m]} * {factors[-m-1]} = {number}")
    flag = input("Run Again (y/n) : ").lower() == 'y'
print("Thank you for using Factor Generator App")
