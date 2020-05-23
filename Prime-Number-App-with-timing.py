import time
import math
print("Welcome to Prime Number App")
flag = True
prime_flag = True
while flag:
    print("Enter 1 to determine whether a particular number is a prime or not.")
    print("Enter 2 to get all the prime number between a specific range.")
    choice = int(input("Enter your choice 1 or 2 : "))
    if choice == 1:
        number = int(input("\nEnter the number : "))
        for i in range(2, math.ceil(math.sqrt(number) + 1)):
            if number == 1:
                print(f"{1} is neither a prime nor a composite")
            if number % i == 0:
                print(f"\n{number} is not a prime")
                prime_flag = False
                break
            prime_flag = True
        if prime_flag:
            print(f"\n{number} is a prime")
    elif choice == 2:
        prime_list = []
        timer = time.time()
        low_number = int(input("\nEnter the lower bound of range : "))
        high_number = int(input("\nEnter the upper bound of range : "))
        for n in range(low_number, high_number):
            for i in range(2, math.ceil(math.sqrt(n) + 1)):
                if n % i == 0:
                    # print(f"\n{number} is not a prime")
                    prime_flag = False
                    break
                prime_flag = True
            if prime_flag:
                prime_list.append(n)
        print(f"\nCalculation took a total time of {round(time.time() - timer, 4)} seconds")
        print(f"The following number between {low_number} and {high_number} are prime :")
        input("Press enter to continue.")
        for m in prime_list:
            print(m)
    else:
        print("That is not a Invalid choice")

    flag = input("Would to like to run program again (y/n) : ") == 'y'
print("Thank you for using this program. Good bye!")
