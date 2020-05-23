print("Welcome to Even Odd Number Sorter App")
number_list = [int(i) for i in input("\nEnter a string of number separated by commas (,) : ").replace(" ", "").split(",")]
odd_list = []
even_list = []
flag = True
while flag:
    print("\n--- Result Summary ---")
    for m in number_list:
        if m % 2 == 0:
            print(f"\t{m} is even!")
            even_list.append(m)
        else:
            print(f"\t{m} is odd!")
            odd_list.append(m)
    print(f"\nThe following {len(even_list)} number are even :")
    for m in even_list:
        print(f"\t{m}")
    print(f"\nThe following {len(odd_list)} number are odd :")
    for m in odd_list:
        print(f"\t{m}")
    flag = input("\nWould you like to run the program again (y/n) : ") == 'y'
print("Thank you for using this program. Goodbye!")
