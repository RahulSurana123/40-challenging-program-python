import datetime
print("Welcome to Grocery List App\n")
print("Current Date and Time " + str(datetime.datetime.now().strftime("%m/%d     %H:%M")))
grocery = ["Panner", "Gobi"]
print("You currently have " + grocery[0] +" and "+ grocery[1] + "in the list")
grocery.append(input("Type of food to be added to the list : ").title())
grocery.append(input("Type of food to be added to the list : ").title())
grocery.append(input("Type of food to be added to the list : ").title())
print("\nHere is your grocery list..")
print(grocery)
grocery.sort()
print("Here is your grocery list sorted")
print(grocery)
print("\nSimulating Grocery Shopping ...")
print("\nCurrent grocery list : " + str(len(grocery))+" items")
print(grocery)
remove_grocery = input("What food did you just buy : ")
print("Removing " + remove_grocery.title() + " from list...")
grocery.remove(remove_grocery.title())
print("\nCurrent grocery list : " + str(len(grocery))+" items")
print(grocery)
remove_grocery = input("What food did you just buy : ")
print("Removing " + remove_grocery.title() + " from list...")
grocery.remove(remove_grocery.title())
print("\nCurrent grocery list : " + str(len(grocery))+" items")
print(grocery)
remove_grocery = input("What food did you just buy : ")
print("Removing " + remove_grocery.title() + " from list...")
grocery.remove(remove_grocery.title())
print("\nCurrent grocery list : " + str(len(grocery))+" items")
print(grocery)
print("\nSorry, store is out of " + grocery[-1])
remove_grocery = input("What food would you like instead : ")
grocery.pop()
grocery.insert(0, remove_grocery.title())
print("Here is what remain in the list:")
print(grocery)


